from django.conf.urls import url
from . import views


app_name = 'state'


urlpatterns = [
    url(r'^getcookie/$', view=views.get_cookie, name='get_cookie'),
    url(r'^setcookie/$', view=views.set_cookie, name='set_cookie'),
    url(r'^deletecookie/$', view=views.delete_cookie, name='delete_cookie'),
]

