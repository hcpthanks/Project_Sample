from django.conf.urls import url
from . import views

app_name = 'feedback'

urlpatterns = [
    url('^$', view=views.home, name='feedback'),
    url('^form/$', view=views.feedback_form, name='feedback_form'),
    url('^list/$', view=views.feedback_list, name='feedback_list'),
    url('(?P<fid>\d{1,4})/$', view=views.feedback_editor, name='feedback_editor'),


]