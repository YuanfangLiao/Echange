from django.urls import path

from goods import views

urlpatterns = [
    path('goods', views.GoodsView.as_view()),
    path('order', views.OrderView.as_view()),
    path('collection', views.CollectionView.as_view())
]
