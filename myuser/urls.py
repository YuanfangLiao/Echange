from django.urls import path

from myuser import views
from myuser import chatView

urlpatterns = [
    path('register', views.RegisterView.as_view()),
    path('login', views.LoginView.as_view()),
    path('info', views.MyUserView.as_view()),
    path('myself', views.MyUserView.as_view()),
    path('change_pass', views.ChangePassView.as_view()),
]
