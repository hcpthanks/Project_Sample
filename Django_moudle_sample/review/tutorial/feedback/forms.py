from django import forms
from .models import Feedback
from django.core.exceptions import ValidationError
from django.core import validators


class FeedbackForm(forms.Form):
    subject = forms.CharField(label='主题', max_length=20,
                              validators=[validators.MinLengthValidator(2, message='主题不得少于2个字符')],
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(label='分类', choices=Feedback.CATEGORIES,
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    username = forms.CharField(label='姓名', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='邮箱', widget=forms.TextInput(attrs={'class': 'form-control'}))
    screenshot = forms.FileField(label='问题截图', required=False)
    description = forms.CharField(label='问题描述', widget=forms.Textarea(attrs={'class': 'form-control'}))
    subscription = forms.BooleanField(label='订阅资讯', required=False )
    status = forms.ChoiceField(label='处理状态', choices=Feedback.STATUS, required=False,
                               widget=forms.Select(attrs={'class': 'form-control'}))
    posted_time = forms.DateTimeField(label='发布 时间', required=False)


class ContactForm(forms.Form):
    username = forms.CharField()
    group = forms.ChoiceField()
    mobile = forms.CharField()
    star = forms.BooleanField()


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(f'数字{value}不是一个偶数')

class TestForm(forms.Form):
    name = forms.CharField(label='姓名', max_length='30',
                           validators=[validators.MinLengthValidator(3, message='最小需要3个字符')])
    email = forms.EmailField(label='邮箱')
    alt_email = forms.CharField(label='备用邮箱',validators=[validators.EmailValidator])
    site = forms.URLField(label='网址')
    mobile = forms.CharField(label='手机号码', validators=[validators.RegexValidator(r'^1(3|4|5|7|8)[0-9]\d{8}$')])
    ip = forms.CharField(label='IP地址', validators=[validators.validate_ipv4_address])
    age = forms.IntegerField(label='年龄', validators=[
        validators.MinLengthValidator(18, message='最小年龄为18岁'),
        validators.MaxLengthValidator(100, message='年龄最大为100岁')
    ])
    price = forms.DecimalField(label='价格')
    number = forms.IntegerField(validators=[validate_even])
