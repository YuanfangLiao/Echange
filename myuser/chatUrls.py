from django.urls import path

from myuser import chatView as views

urlpatterns = [
    path('getlist', views.ChatListView.as_view()),
    path('msg', views.ChatMsgView.as_view())
]
