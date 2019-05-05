from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from goods.models import Goods, Order, MyCollection
from goods.serializers import GoodsSerializer, OrderSerializer, CollectionSerializer


class GoodsView(APIView):
    # authentication_classes = (BasicAuthentication, SessionAuthentication, TokenAuthentication)
    # permission_classes = (IsAuthenticated,)

    # 获取商品，默认获取全部商品
    def get(self, request):
        id = request.query_params.get('id')
        order_id = request.query_params.get('order_id')
        query = request.query_params.get('query')
        goods = Goods.objects.all().filter(active=True)
        # ser_obj = None
        # 如果是使用order查询goods
        if order_id:
            order = Order.objects.filter(pk=order_id).first()
            goods = Goods.objects.filter(pk=order.goods_id)
        # 如果查询是查询'我的商品'，把不活跃的也发布出去
        if query == 'mine':
            goods = Goods.objects.all().filter(publisher=request.user)
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
        # 如果是主页
        elif query == 'index':
            goods = goods.order_by('-create_time')
            if len(goods) > 50:
                goods = goods[:50]
        else:
            if id:
                goods = Goods.objects.filter(pk=id)
            else:
                goods = goods.order_by('-create_time')
        ser_obj = GoodsSerializer(goods, many=True)
        print(ser_obj.data)
        return Response(ser_obj.data)

    # 增加商品时调用
    def post(self, request):
        good_obj = request.data
        print(good_obj)
        # good_obj['publisher'] = request.user.id
        try:
            Goods.objects.create(title=good_obj.get('title'), type=good_obj.get('type'),
                                 price=good_obj.get('price'), brand=good_obj.get('brand'),
                                 condition=good_obj.get('condition'), picture=good_obj.get('picture'),
                                 detail=good_obj.get('detail'), want=good_obj.get('want'),
                                 publisher=request.user)
            return Response({'flag': 'success'})
        except Exception as e:
            return Response({'flag': 'error', 'error': str(e)})

    def put(self, request):
        req_data = request.data
        query = request.data.get('query')
        print(query)
        # 重新发布
        if query == 'republish':
            Goods.objects.filter(id=req_data.get('id')).update(active=True)
            print('success')
            return Response({'flag': 'success'})

        try:
            Goods.objects.filter(id=req_data.get('id')).update(title=req_data.get('title'),
                                                               type=req_data.get('type'),
                                                               price=req_data.get('price'),
                                                               brand=req_data.get('brand'),
                                                               condition=req_data.get('condition'),
                                                               picture=req_data.get('picture'),
                                                               detail=req_data.get('detail'),
                                                               want=req_data.get('want'))
            # print(req_data)
            return Response({'flag': 'success'})
        except Exception as e:
            return Response({'flag': 'error', 'error': str(e)})

    def delete(self, request):
        id = request.data.get('id')
        goods_obj = Goods.objects.filter(pk=id)
        goods_obj.update(active=False)
        return Response({'flag': 'success'})


class OrderView(APIView):
    authentication_classes = (BasicAuthentication, SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        id = request.query_params.get('id')
        query = request.query_params.get('query')
        # 如果查询是查询'我的购买'
        if query == 'mine':
            orders = Order.objects.filter(buyer=request.user)
            ser_obj = OrderSerializer(orders, many=True)
            print(ser_obj.data)
            return Response(ser_obj.data)
        elif query == 'mySell':
            goods_queryset = Goods.objects.filter(publisher=request.user)
            orders = Order.objects.filter(goods__in=goods_queryset)
            ser_obj = OrderSerializer(orders, many=True)
            print(ser_obj.data)
            return Response(ser_obj.data)
        else:
            if id:
                orders = Order.objects.filter(pk=id)
            else:
                orders = Order.objects.all()
            ser_obj = OrderSerializer(orders, many=True)
            return Response(ser_obj.data)

    def post(self, request):
        order_obj = request.data
        good_obj = Goods.objects.filter(pk=order_obj.get('goods_id')).first()
        publisher = good_obj.publisher
        if publisher == request.user:
            return Response({'flag': 'error', 'error': '不能申请自己发布的物品'})
        try:
            Order.objects.create(msg=order_obj.get('msg'), buyer=request.user, goods_id=order_obj.get('goods_id'))
            return Response({'flag': 'success'})
        except Exception as e:
            return Response({'flag': 'error', 'error': str(e)})

    def put(self, request):
        id = request.data.get('id')
        msg = request.data.get('msg')
        status = request.data.get('status')
        order_obj = Order.objects.filter(pk=id)
        if msg:
            order_obj.update(msg=msg)
        if status:
            if status == 2:
                # 达成交易就把商品状态变成禁用
                goods_obj = order_obj.first().goods
                goods_obj.active = False
                goods_obj.sold = True
                goods_obj.save()
            order_obj.update(status=status)
        return Response({'flag': 'success'})


class CollectionView(APIView):
    authentication_classes = (BasicAuthentication, SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        id = request.query_params.get('id')
        query = request.query_params.get('query')
        # 说明是查询自己的收藏记录
        if query == 'mine':
            collection_queryset = MyCollection.objects.filter(user=request.user).order_by('-create_time')
            ser_obj = CollectionSerializer(collection_queryset, many=True)
            print(ser_obj.data)
            return Response(ser_obj.data)
        else:
            user = request.user
            collection_queryset = MyCollection.objects.filter(goods_id=id, user=user)
            print(id, user)
            if collection_queryset:
                return Response({'flag': 'success', 'msg': True})
            return Response({'flag': 'success', 'msg': False})

    # 添加收藏
    def post(self, request):
        id = request.data.get('id')
        user = request.user
        collection_queryset = MyCollection.objects.filter(goods_id=id, user=user)
        print(id)
        if collection_queryset:
            collection_queryset.delete()
            return Response({'flag': 'success', 'msg': '取消收藏成功'})
        MyCollection.objects.create(user=user, goods_id=id)
        return Response({'flag': 'success', 'msg': '收藏成功'})

    # 删除收藏
    def delete(self, request):
        id = request.data.get('id')
        collection = MyCollection.objects.filter(id=id)
        print(id)
        collection.delete()
        return Response({'flag': 'success'})
