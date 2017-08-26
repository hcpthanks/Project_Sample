from django.contrib import admin
from .models import Message

# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    """留言信息管理
    """
    list_display  = ('name', 'email', 'active', 'posted')
    list_filter   = ('active','posted')
    search_fields = ('name', 'message')
    ordering      = ('-posted',)


#注册留言管理
admin.site.register(Message, MessageAdmin)



