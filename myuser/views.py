from django.contrib.auth import authenticate, login
from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from myuser.models import MyUser
from myuser.serializers import MyUserSerializer


class RegisterView(APIView):
    def post(self, request):
        data = dict(request.data)
        print(data)
        username = data.get('username')
        passwd = data.get('passwd')
        confpasswd = data.get('confpasswd')
        phone = data.get('phone')
        email = data.get('email')
        sex = data.get('sex')
        if not (username and passwd and confpasswd and phone and email and sex):
            return Response({'code': 406, 'error': '请输入所有必填项'})
        if passwd != confpasswd:
            return Response({'code': 406, 'error': '请输入两次相同的密码'})
        if len(passwd) < 6:
            return Response({'code': 406, 'error': '密码需要在6位数以上'})
        try:
            MyUser.objects.create_user(username=username, password=passwd, phone=phone, email=email, sex=sex)
        except Exception as e:
            return Response({'code': 500, 'error': str(e)})
        return Response({'code': 200})

    def get(self, request):
        print(request.data)
        return Response({'code': 200})


class LoginView(APIView):
    def post(self, request):
        data = dict(request.data)
        username = data.get('username')
        passwd = data.get('password')
        user = authenticate(username=username, password=passwd)
        if user:
            login(request, user)
            # print(request.session.get())
            return Response({'code': 200, 'flag': 'success'})
        else:
            return Response({'code': 200, 'flag': 'fail', 'msg': '用户名/密码错误'})


class MyUserView(APIView):
    authentication_classes = (BasicAuthentication, SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        ser_user = MyUserSerializer(user)
        return Response(ser_user.data)
