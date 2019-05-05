# Create your models here.
from django.db import models
from django.db.models import DO_NOTHING


class Carousel(models.Model):
    name = models.CharField(u'图片名称', max_length=30, null=False)
    img = models.ImageField(u'图片', upload_to='carousel')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '主页轮播图'
