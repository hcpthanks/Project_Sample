from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField('姓名', max_length=50)
	email = models.EmailField('邮箱', max_length=255)
	mobile = models.CharField('手机', max_length=20)
	pub_date = models.DateTimeField('发布时间')


	def __str__(self):
		return self.name

