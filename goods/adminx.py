import xadmin

from goods.models import Goods, Order


class GoodsAdminx(object):
    list_display = ('title', 'id', 'type', 'active', 'sold')
    exclude = ('picture', 'publisher', '')
    # model_icon = 'fa fa-edit'


class OrderAdminx(object):
    list_display = ('id', 'status', 'buyer', 'goods')


xadmin.site.register(Goods, GoodsAdminx)
xadmin.site.register(Order, OrderAdminx)
