import os

from django.http import JsonResponse
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from DjangoGoodsExchange.settings import MEDIA_ROOT
from app.models import Carousel
from app.serializers import CarouselSerializer
from goods.models import Goods
import numpy as np
import pandas as pd
from sklearn.externals import joblib


def api(request):
    goods = Goods.objects.all()
    now_goods = goods.first()
    my_list = []
    for i in goods:
        my_list.append([i.id, i.type, i.price, i.condition, now_goods.type,
                        now_goods.price, now_goods.condition, abs(i.type - now_goods.type),
                        (i.price - now_goods.price) / ((i.price + now_goods.price) / 2),
                        (i.condition - now_goods.condition) / 50])
        # my_list.append()
    print(my_list)
    dfoff = pd.DataFrame(my_list)
    dfoff.columns = ['id', '分类1', '价格1', '成色1', '分类2', '价格2', '成色2', 'classification', 'price', 'new']
    print(dfoff)
    clf = joblib.load(os.path.join(MEDIA_ROOT, 'filename.pkl'))
    feature = ['classification', 'price', 'new']
    predictors = feature
    a = clf.predict(dfoff[predictors])
    print(a)
    return JsonResponse({'code': 200})
