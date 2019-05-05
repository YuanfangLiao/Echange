import os
import random

from PIL import Image
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from DjangoGoodsExchange import settings
from app.models import Carousel
from app.serializers import CarouselSerializer
from goods.models import Goods, Order

# 通用获取所有分类信息接口
from goods.serializers import GoodsSerializer


# 通用获取所有种类的接口
def get_all_goods_type(request):
    all = Goods.GOODS_TYPE
    data = []
    for key, value in all:
        data.append({
            'value': key,
            'label': value
        })

    return JsonResponse({'code': 200, 'data': data}, json_dumps_params={'ensure_ascii': False})


# 通用上传照片接口
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


# 通用删除照片接口
def del_pic(request):
    if request.method == 'POST':
        # print(request.POST.get('url'))
        url = request.POST.get('url')
        url = os.path.join(settings.MEDIA_ROOT, url)
        os.remove(url)
        print('删除一张照片')
        return JsonResponse({'flag': 'success'})


# 用于前端检查该某用户有没有对某商品下过单
class UserOrderCheckApi(APIView):
    def get(self, request):
        goods_id = request.query_params.get('id')
        user = request.user
        order = Order.objects.filter(buyer=user, goods_id=goods_id)
        if order:
            # 已经有记录了，阻止进入
            return Response({'flag': 'fail', 'msg': '你已经提交过这个产品的交换意向了'})
        else:
            return Response({'flag': 'success'})


class SimilarGoodsApi(APIView):

    # 同类推荐算法
    def get(self, request):
        id = request.query_params.get('id')
        goods = Goods.objects.filter(pk=id).first()
        type = goods.type
        goods_queryset = Goods.objects.filter(type=type).exclude(pk=id).order_by('-create_time')
        if not goods_queryset:
            goods_queryset = Goods.objects.all().order_by('-create_time')
        if len(goods_queryset) > 5:
            goods_queryset = goods_queryset[:5]

        ser_obj = GoodsSerializer(goods_queryset, many=True)
        return Response(ser_obj.data)


class CarouselView(APIView):

    def get(self, request):
        carousels_obj = Carousel.objects.all()
        ser_obj = CarouselSerializer(carousels_obj, many=True)
        return Response(ser_obj.data)


class SearchGoodsView(APIView):

    def get(self, request):
        id = request.query_params.get('id')
        query = request.query_params.get('query')
        kw = request.query_params.get('kw')
        goods = Goods.objects.all().filter(active=True)
        try:
            goods = goods.filter(Q(title__contains=kw) | Q(publisher__address__contains=kw) |
                                 Q(want__contains=kw) | Q(detail__contains=kw) | Q(pk=int(kw)))
        except Exception:
            goods = goods.filter(Q(title__contains=kw) | Q(publisher__address__contains=kw) |
                                 Q(want__contains=kw) | Q(detail__contains=kw))

        if query == 'sort':
            prop = request.query_params.get('prop')
            order = request.query_params.get('order')
            print(type(order))
            left = ''
            # final = ''
            if order == 'descending':
                left = '-'
            elif order == 'ascending':
                left = ''
            # 只有两个排序条件都有才进行排序
            if prop and order:
                final = left + prop
                print(final)
                goods = goods.order_by(final)
        #  如果是过滤器
        elif query == 'filter':
            filters = request.query_params.get('filters')
            filters = eval(filters)
            goods = goods.filter(type__in=filters)

        else:
            goods = goods.order_by('-create_time')
            if len(goods) > 50:
                goods = goods[:50]
        ser_obj = GoodsSerializer(goods, many=True)
        print(ser_obj.data)
        return Response(ser_obj.data)
