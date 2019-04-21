from django.urls import path

from goods import views

urlpatterns = [
    path('goods', views.GoodsView.as_view())
]
