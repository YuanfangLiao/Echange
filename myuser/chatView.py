import json
import time

from django.db.models import Q
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from myuser.models import Chat
from myuser.serializers import ChatSerializer, MyUserSerializer


# 用作展示聊天列表的视图
class ChatListView(APIView):
    authentication_classes = (BasicAuthentication, SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        id = request.query_params.get('id')
        # 获取聊天详情
        if id:
            chat_obj = Chat.objects.filter(pk=id).first()
            if chat_obj.user1 == request.user:
                return Response(MyUserSerializer(chat_obj.user2).data)
            else:
                return Response(MyUserSerializer(chat_obj.user1).data)
        # 获取用户聊天列表
        else:
            user = request.user
            # 返回和用户相关的聊天信息
            chat_obj = Chat.objects.filter(Q(user1=user) | Q(user2=user))
            ser_obj = ChatSerializer(chat_obj, many=True)
            # print(type(ser_obj.data))
            return Response(ser_obj.data)

    def post(self, request):
        pass


# 用作处理聊天数据，主要是聊天的内容的视图
class ChatMsgView(APIView):
    authentication_classes = (BasicAuthentication, SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        id = request.query_params.get('id')
        chat_obj = Chat.objects.filter(pk=id).first()
        msg_obj = eval(chat_obj.msg)
        return Response({'msg': msg_obj})

    def put(self, request):
        data = request.data
        msg = data.get('msg')
        id = data.get('id')
        chat_obj = Chat.objects.filter(pk=id).first()
        old_msg_obj = chat_obj.msg
        if not old_msg_obj:
            my_json_obj = []
        else:
            my_json_obj = eval(old_msg_obj)

        # 判断一下原有消息队列长度，如果太长了，需要优化性能，去掉队头的一条数据
        if len(my_json_obj) > 50:
            my_json_obj = my_json_obj[-49:]
        # 开始创建新的聊天记录
        now_time = time.strftime('%Y.%m.%d %H:%M:%S')
        my_dict_obj = {}
        my_dict_obj['time'] = now_time
        my_dict_obj['img'] = request.user.picture
        my_dict_obj['username'] = request.user.username
        my_dict_obj['msg'] = msg

        my_json_obj.append(my_dict_obj)
        print(json.dumps(my_json_obj))
        chat_obj.msg = json.dumps(my_json_obj)
        chat_obj.save()
        return Response({'flag': 'success'})
