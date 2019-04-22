from django.contrib.auth import authenticate, login

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

    def put(self, request):
        user = request.user
        ser_obj = MyUserSerializer(user, data=request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            print(ser_obj.validated_data)
            return Response({'flag': 'success'})
        print(ser_obj.errors)
        return Response(ser_obj.errors)


class ChangePassView(APIView):
    authentication_classes = (BasicAuthentication, SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user
        data = request.data
        username = user.username
        if data.get('new_passwd') != data.get('conf_passwd'):
            return Response({'flag': 'error', 'msg': '请输入两次一样的密码'})
        auth_user = authenticate(username=username, password=data.get('old_passwd'))
        if not auth_user:
            return Response({'flag': 'error', 'msg': '旧密码错误'})
        user.set_password(data.get('new_passwd'))
        user.save()
        return Response({'flag': 'success'})
