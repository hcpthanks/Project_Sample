from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms import validators


class UserRegForm(Form):
    username = StringField('用户名', [validators.DataRequired('用户名必填'),validators.length(min=4,max=20,message='用户名必须介于4-20个字之间')])
    email = StringField('邮箱', [validators.Email('邮箱格式不正确')])
    password = PasswordField('密码', [validators.DataRequired('密码必填'), validators.length(min=6, max=20, message='密码长度必须介于6-20个字符')])
    confirm = PasswordField('重复密码', [validators.EqualTo('password', message='两次密码输入不一致')])
    accept = BooleanField('接受协议', [validators.DataRequired('同意协议后才可以注册')])