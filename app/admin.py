from django.contrib import admin

from app.models import Carousel

# Register your models here.

#
# for table in models.__all__:
#     admin.site.register(getattr(models, table))

admin.site.register(Carousel)
