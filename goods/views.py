from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from goods.models import Goods
from goods.serializers import GoodsSerializer


class GoodsView(APIView):
    # authentication_classes = (BasicAuthentication, SessionAuthentication, TokenAuthentication)
    # permission_classes = (IsAuthenticated,)

    # 获取商品，默认获取全部商品
    def get(self, request):
        goods_queryset = Goods.objects.all()
        ser_obj = GoodsSerializer(goods_queryset, many=True)
        return Response(ser_obj.data)

    # 增加商品时调用
    def post(self, request):
        good_obj = request.data
        print(good_obj)
        ser_obj = GoodsSerializer(data=good_obj)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response({'flag': 'success'})
        return Response(ser_obj.errors)
