from django.conf.urls import url
from . import views

app_name = 'templates'

urlpatterns = [
    url('^$', view=views.home, name='templates'),
    url('^get_feedback_data/$', view=views.get_feedback_data, name='get_feedback_data'),


]