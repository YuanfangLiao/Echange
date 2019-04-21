from django.urls import path

from myuser import views

urlpatterns = [
    path('register', views.RegisterView.as_view()),
    path('login', views.LoginView.as_view()),
    path('info', views.MyUserView.as_view())
]
