from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader  # 导入载入器
from .models import Contact  # 从同级的models导入写好的类

 def index(request):
     """"模拟载入列表""
    template = loader.get_template('contacts/index.html')   #从载入器获得模板index.html
    context = {'contact_list': ['aaa', 'bbb', 'ccc']}       #上下文模拟数据
    return HttpResponse(template.render(context, request))  #模板渲染呈现上下文


def detail(request, contact_id):
    return HttpResponse('联系人详情页')


==========
index.html
==========
    <h1> 通讯录首页</h1>
    <ul>
        #遍历从后台传递过来的模拟上下文context里的contact_list
        {% for contact in contact_list %}
            <li><a href="">{{ contact}}</a></li>    #前端呈现 模拟上下文
        {% endfor %}
    </ul>

      <ul>
        {% for contact in contact_list %}           #遍历数据库传递过来的上下文contact_list
            #前端呈现 数据库上下文
            <li><a href="/contact/{{contact.id}}/">{{ contact.name}} - {{contact.mobile}}</a></li>
        {% endfor %}
    </ul>
============
detail.html
============
    <p>姓名:{{ contact.name}} <br> 邮箱:{{ contact.email}} <br> 手机:{{ contact.mobile}} </p>



============


def index(request):
    """载入数据库真实数据"""
    contact_list = Contact.objects.all()      #变量contact_list得到所有的联系人信息
    template = loader.get_template('contacts/index.html') 
    context = {'contact_list': contact_list}   #上下文等于一个字典表,键值叫'contact_list' 赋予变量contact_list
    return HttpResponse(template.render(context, request))


def detail(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)   #接收从url传递过来的参数contact_id 到数据库查询contact(假定一切正常)
    template = loader.get_template("contacts/detail.html")  #获取模板
    context = {'contact': contact}                          #准备上下文 获取数据
    return HttpResponse(template.render(context, request))  #呈现上下文


==========================
python manage.py createsuperuser 创建超级用户

=============
admin.py 模块
=============
from django.contrib import admin
from .models import Contact   #导入models下的类Contact

admin.site.register(Contact)   #在后台站点注册Contact
