from rest_framework import serializers

from myuser.models import MyUser


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email', 'phone', 'address', 'level', 'credit', 'sex', 'user_type')
