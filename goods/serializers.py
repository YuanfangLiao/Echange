from rest_framework import serializers

from goods.models import Goods


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = "__all__"
