from django.conf.urls import url
from . import views

app_name = 'hello'

urlpatterns = [
    url(r'^home/$', view=views.home, name='hello-home'),
    url(r'^course/(\d{4})/$', view=views.course_year, name='hello-course_year'),
    url(r'^course/(\d{4})/(\d{2})/$', view=views.course_year_month, name='hello-course_year_month'),
    url(r'^redirect/$', view=views.view_redirect, name='course_redirect'),
    url(r'^contact/$', view=views.view_contact, name='contact'),
    url(r'^product/(?P<pid>\d+)/$', view=views.product_info, name='product_detail'),
    url(r'^help/$', view=views.help_center, name='help'),
    url(r'^request/$', view=views.request_info, name='request_info'),
]