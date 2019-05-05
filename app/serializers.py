from rest_framework import serializers

from app.models import Carousel


class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = "__all__"
