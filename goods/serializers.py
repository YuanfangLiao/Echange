from rest_framework import serializers

from goods.models import Goods, Order, MyCollection
from myuser.serializers import MyUserSerializer


class GoodsSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField(read_only=True)
    type = serializers.SerializerMethodField(read_only=True)
    type_key = serializers.SerializerMethodField(read_only=True)
    publisher = MyUserSerializer()

    def get_picture(self, obj):
        # 序列化的时候，把字符串转换成js的Array
        picture_list = obj.picture.split('$$$')[:-1]
        # print(obj.title + ': ', picture_list)
        return picture_list

    def get_type_key(self, obj):
        return obj.type

    def get_type(self, obj):
        all = Goods.GOODS_TYPE
        data = {}
        for key, value in all:
            data[key] = value
        res = data[obj.type]
        return res

    class Meta:
        model = Goods
        # depth = 1
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()
    status = serializers.SerializerMethodField(read_only=True)

    def get_status(self, obj):
        all = Order.ORDER_STATUS
        data = {}
        for key, value in all:
            data[key] = value
        res = data[obj.status]
        return res

    # goods = serializers.PrimaryKeyRelatedField(e)

    class Meta:
        model = Order
        # depth = 1
        fields = "__all__"
        read_only_fields = ('id', 'msg', 'status', 'create_time')


class CollectionSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()
    user = MyUserSerializer()

    class Meta:
        model = MyCollection
        fields = '__all__'
