from django.db import models

""" PMS 产品相关模型类
"""


class Category(models.Model):
    name = models.CharField('类型名称', max_length=20)
    description = models.CharField('备注说明', max_length=100, null=True)

    def __str__(self):
        return f'{self.id} { self.name}'


class Product(models.Model):
    name = models.CharField('名称', max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    quantity_per_unit = models.CharField('单位数量', max_length=50)
    unit_price = models.DecimalField('单价', max_digits=10, decimal_places=2)
    units_in_stock = models.IntegerField('库存数量', default=0)
    discountinued = models.BooleanField('停产', default=False)
    updated_time = models.DateTimeField('最后更新', auto_now=True)
    posted_time = models.DateTimeField('发布时间', auto_now_add=True)

    def __str__(self):
        return f'{self.id} - {self.name} - {self.unit_price} - {self.category.name}'

    class Meta:
        ordering = ['-unit_price']