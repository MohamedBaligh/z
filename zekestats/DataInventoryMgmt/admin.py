from django.contrib import admin

# Register your models here.

from .models import Category, DataSet

admin.site.register(Category)
admin.site.register(DataSet)

