from django.conf.urls import url
from . import views

app_name = 'templates'

urlpatterns = [
    url('^$', view=views.home, name='feedback'),
    url('^form/$', view=views.feedback_form, name='feedback_form'),


]