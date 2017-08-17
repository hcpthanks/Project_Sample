from django import forms
from .models import Feedback


class FeedbackForm(forms.Form):
    subject = forms.CharField(label='主题', widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(label='分类', choices=Feedback.CATEGORIES,
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='邮箱', widget=forms.TextInput(attrs={'class': 'form-control'}))
    screenshot = forms.FileField(label='问题截图')
    description = forms.CharField(label='问题描述', widget=forms.Textarea(attrs={'class': 'form-control'}))
    subscription = forms.BooleanField(label='订阅资讯')
    status = forms.ChoiceField(label='处理状态', choices=Feedback.STATUS,
                               widget=forms.Select(attrs={'class': 'form-control'}))
    posted_time = forms.DateTimeField(label='发布时间')





class ContactForm(forms.Form):
    username = forms.CharField()
    group = forms.ChoiceField()
    mobile = forms.CharField()
    star = forms.BooleanField()