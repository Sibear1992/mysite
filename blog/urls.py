from django.conf.urls import url, include
from .views import *
urlpatterns = [
    url(r'^', posts, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', post_detail, name='post_detail'),
]