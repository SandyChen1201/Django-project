from django.contrib import admin
from .models import Todo

# Register your models here.
# 在本地引用需要from. 才找的到自己新增的模型
admin.site.register(Todo)
