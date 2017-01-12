from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^about/$', views.about_show, name='about_show'),
    url(r'^project/$', views.project_list, name='project_list'),
    url(r'^other/$', views.other_list, name='other_list'),
    url(r'^contact/$', views.contact_list, name='contact_list'),
]
