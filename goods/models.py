from django.db import models

# Create your models here.

# 限制IntegerField的最大最小值
from myuser.models import MyUser


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Goods(models.Model):
    title = models.CharField(u'简介', max_length=50)
    GOODS_TYPE = ((1, '数码产品'), (2, '日用品'), (3, '服饰'), (5, '学习用品'), (4, '其他'),)
    type = models.IntegerField(u'分类', choices=GOODS_TYPE)
    active = models.BooleanField(u'是否活跃', default=True)
    sold = models.BooleanField(u'是否被销售', default=False)
    price = models.FloatField(u'价格')
    brand = models.CharField(u'品牌', max_length=50)
    condition = IntegerRangeField(u'新旧成色', max_value=100, min_value=10)
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    picture = models.CharField(u'图片路径', max_length=1000)
    detail = models.TextField(u'详细介绍', max_length=2000, null=True)
    want = models.CharField(u'想换的', max_length=1000, null=True)
    publisher = models.ForeignKey(to=MyUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '商品'


class Order(models.Model):
    buyer = models.ForeignKey(MyUser, verbose_name='购买者', on_delete=models.CASCADE, null=True)
    goods = models.ForeignKey(Goods, verbose_name='商品', on_delete=models.CASCADE, null=True)
    msg = models.CharField(u'留言', max_length=200, null=True)
    ORDER_STATUS = ((1, '待沟通'), (2, '确认交易'), (3, '交易终止'), (4, '交易成功'))
    status = models.IntegerField(u'交易状态', choices=ORDER_STATUS, default=1)
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = '订单'


# 收藏表
class MyCollection(models.Model):
    goods = models.ForeignKey(Goods, verbose_name='商品', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(MyUser, verbose_name='收藏者', on_delete=models.CASCADE, null=True)
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    def __str__(self):
        return self.user.username + self.goods.title

    class Meta:
        verbose_name_plural = '收藏'
