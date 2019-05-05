import xadmin
from django.contrib.auth.models import Group, Permission
from xadmin import views
from xadmin.models import UserWidget, UserSettings

from app.models import Carousel
from myuser.models import MyUser


class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True


class GlobalSetting(object):
    site_title = 'Echange物品交换平台后台管理系统'  # 修改首页标题
    site_footer = 'Qingdao University'  # 修改首页页脚标题
    menu_style = 'default'  # 'accordion'


class CarouselAdminx(object):
    list_display = ('id', 'name', 'img')
    # model_icon = 'fa fa-edit'


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.sites.site.register(views.CommAdminView, GlobalSetting)

# 不要自带的权限控制
xadmin.site.unregister(Permission)
xadmin.site.unregister(Group)

xadmin.sites.site.register(Carousel, CarouselAdminx)
