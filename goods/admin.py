from django.contrib import admin

# Register your models here.
from goods import models

admin.site.register(getattr(models, "Goods"))