"""DjangoGoodsExchange URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

import xadmin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views as drf_views
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from DjangoGoodsExchange.settings import BASE_DIR
from app import views
from myuser import urls as user_url
from myuser import chatUrls as chat_url
from goods import urls as goods_url
from app import urls as api_url

urlpatterns = [path('admin/', admin.site.urls),
               path('xadmin/', xadmin.site.urls),
               # drf token验证
               path('api-token-auth', drf_views.obtain_auth_token),
               # re_path('^v1/', TemplateView.as_view(template_name="index.html")),

               path('api_test', views.api),
               path('user/', include((user_url, 'myuser'), namespace='myuser')),
               path('chat_api/', include((chat_url, 'myuser'), namespace='chat')),
               # goods名字起的不太合理，给一个另外的名字的接口
               path('goods/', include((goods_url, 'goods'), namespace='goods')),
               path('goods_api/', include((goods_url, 'goods'), namespace='shop')),
               # 通用api写在这里
               path('api/', include((api_url, 'app'), namespace='app')),
               # re_path('^.*?$', TemplateView.as_view(template_name="index.html")),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static('/frontend/', document_root=os.path.join(BASE_DIR, 'frontend'))
