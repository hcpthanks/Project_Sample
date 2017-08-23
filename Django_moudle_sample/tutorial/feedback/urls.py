from django.conf.urls import url
from . import views

app_name = 'feedback'

urlpatterns = [
    url('^$', view=views.home, name='feedback'),
    url('^form/$', view=views.feedback_form, name='feedback_form'),
    url('^login/$', view=views.login, name='login'),
    url('^logout/$', view=views.logout, name='logout'),
    url('^list/$', view=views.feedback_list, name='feedback_list'),
    url('^(?P<fid>\d{1,4})/$', view=views.feedback_editor, name='feedback_editor'),
    url('^edit/(?P<fid>\d{1,4})/$', view=views.feedback_edit, name='feedback_edit'),
    url('^delete/(?P<fid>\d{1,4})/$', view=views.feedback_delete, name='feedback_delete'),


]