from django.conf.urls import url
from app1 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^edit/(?P<ipaddress_id>\d+)/$', views.edit, name='edit'),
    url(r'^add/$', views.edit, name='add'),

]
