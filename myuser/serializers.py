from rest_framework import serializers

from myuser.models import MyUser, Chat


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email', 'phone', 'address',
                  'level', 'credit', 'sex', 'user_type', 'picture',
                  'signature')


class ChatSerializer(serializers.ModelSerializer):
    user1 = MyUserSerializer()
    user2 = MyUserSerializer()

    class Meta:
        model = Chat
        # fields = '__all__'
        exclude = ('msg',)
