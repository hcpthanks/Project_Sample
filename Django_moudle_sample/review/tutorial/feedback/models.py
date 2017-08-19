from django.db import models

# Create your models here.


class Feedback(models.Model):
    CATEGORIES = (
        ('产品质量', '产品质量'),
        ('网站使用', '网站使用'),
        ('支付购买', '支付购买'),
        ('客户服务', '客户服务'),
    )

    STATUS = (
        ('未处理', '未处理'),
        ('处理中', '处理中'),
        ('已处理', '已处理'),
    )

    subject = models.CharField('主题', max_length=100)
    category = models.CharField('分类', choices=CATEGORIES, max_length=20)
    username = models.CharField('姓名', max_length=50)
    email = models.EmailField('邮箱', max_length=100)
    screenshot = models.FileField('问题截图')
    description = models.TextField('问题描述')
    subscription = models.BooleanField('是否订阅', default=True)
    status = models.CharField('处理状态', choices=STATUS, max_length=20)
    posted_time = models.DateTimeField('提交时间', auto_now_add=True)






