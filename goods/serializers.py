from rest_framework import serializers

from goods.models import Goods
from myuser.serializers import MyUserSerializer


class GoodsSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField(read_only=True)
    type = serializers.SerializerMethodField(read_only=True)
    publisher = MyUserSerializer()

    def get_picture(self, obj):
        print(obj.picture)
        # 序列化的时候，把字符串转换成js的Array
        picture_list = obj.picture.split('$$$')[:-1]
        print(picture_list)
        return picture_list

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
