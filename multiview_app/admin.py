from django.contrib import admin
from models import ImageDetail
# Register your models here.

myModels = [ImageDetail]
admin.site.register(myModels)
