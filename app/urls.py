from django.urls import path

from app import views
from app import commomView

urlpatterns = [
    path('all_goods_type', commomView.get_all_goods_type),
    path('upload_pic', commomView.upload_pic),
    path('del_pic', commomView.del_pic),
    path('similar_goods', commomView.SimilarGoodsApi.as_view())
]
