from django.contrib import admin
from .models import Product, Category

# Register your models here.


# 1)定义模型管理类
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


# 2)注册模型管理类到站点管理
admin.site.register(Category,CategoryAdmin)
# admin.site.register(Product, ProductAdmin)


