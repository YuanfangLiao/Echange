from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class MyUser(AbstractUser):
    # 用户类型
    USER_TYPE_CHOICE = ((1, "normal"), (2, "admin"))
    user_type = models.IntegerField(choices=USER_TYPE_CHOICE, null=False, default=1)
    # 性别
    USER_SEX_CHOICE = ((1, '男'), (2, '女'))
    sex = models.IntegerField(choices=USER_SEX_CHOICE, null=False, default=1)
    # 用户手机号,
    phone = models.CharField('手机号', max_length=11, null=True)
    # 用户联系方式
    address = models.CharField('地址', max_length=50, null=True, default='用户还没有设置地址')
    level = models.IntegerField('用户级别', default=1, null=True)
    credit = models.IntegerField('信用分', default=300, null=True)
    picture = models.CharField('头像', max_length=500, default='img/timg.jpg')
    signature = models.CharField('个性签名', max_length=200, default='这个人很懒，什么都没留下')

    def __str__(self):
        return self.username

    class Meta:
        # managed = False
        db_table = 'my_user'
