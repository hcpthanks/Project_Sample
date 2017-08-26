from django.db import models
import reprlib

# Create your models here.

class Message(models.Model):
    """留言信息类
    """
    name = models.CharField('用户名', max_length=20)
    email = models.EmailField('邮箱', max_length=200)
    message = models.TextField('留言')
    active = models.BooleanField('有效', default=True)
    posted = models.DateTimeField('发布时间', auto_now_add=True)


    def __str__(self):
        return f'{self.name} {reprlib.repr(self.message)}'
