from django.conf.urls import *
from . import views

urlpatterns = [
    url(r'^$', views.home, name='main_home'),
    url(r'^article/([0-9]+)/$', views.article, name='main_article'), #old way is url(r'^article/([0-9]+)/$', 'main.views.article'),
]
