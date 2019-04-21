import os
import random

from PIL import Image
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response

from DjangoGoodsExchange import settings
from goods.models import Goods


# 通用获取所有分类信息接口
def get_all_goods_type(request):
    all = Goods.GOODS_TYPE
    data = []
    for key, value in all:
        data.append({
            'value': key,
            'label': value
        })

    return JsonResponse({'code': 200, 'data': data}, json_dumps_params={'ensure_ascii': False})


def upload_pic(request):
    if request.method == 'POST':
        data = request.FILES['file']
        img = Image.open(data)
        width = img.width
        height = img.height
        rate = 1.0  # 压缩率

        # 根据图像大小设置压缩率
        if width >= 2000 or height >= 2000:
            rate = 0.3
        elif width >= 1000 or height >= 1000:
            rate = 0.5
        elif width >= 500 or height >= 500:
            rate = 0.9

        width = int(width * rate)  # 新的宽
        height = int(height * rate)  # 新的高

        img.thumbnail((width, height), Image.ANTIALIAS)  # 生成缩略图
        url = os.path.join('img', data.name)
        absolute_path = os.path.join(settings.MEDIA_ROOT, url)
        while os.path.exists(absolute_path):
            file, ext = os.path.splitext(data.name)
            file = file + str(random.randint(1, 1000))
            data.name = file + ext
            url = os.path.join('img', data.name)
            absolute_path = os.path.join(settings.MEDIA_ROOT, url)

        img.save(absolute_path)
        print(url)
        return JsonResponse({'flag': 'success', 'url': url}, json_dumps_params={'ensure_ascii': False})


def del_pic(request):
    if request.method == 'POST':
        # print(request.POST.get('url'))
        url = request.POST.get('url')
        url = os.path.join(settings.MEDIA_ROOT, url)
        os.remove(url)
        print('删除一张照片')
        return JsonResponse({'flag': 'success'})
