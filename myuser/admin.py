from django.contrib import admin

# Register your models here.
from myuser import models
from myuser.models import MyUser

admin.site.register(getattr(models, "MyUser"))
