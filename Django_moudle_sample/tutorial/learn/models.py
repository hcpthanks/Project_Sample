from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField('姓名', max_length=20)
    email = models.EmailField('邮箱', max_length=100)
    mobile = models.CharField('手机', max_length=20)

    def __str__(self):
        return f'<Contact {self.name}>'

