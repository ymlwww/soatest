"""soatest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from yml import views as yml_views
from likes import views as likes_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^likes/likes_change$',likes_views.likes_change,name='likes_change'),
    url(r'^likes/likes_nums$',likes_views.likes_nums,name='likes_nums'),
    url(r'^list/$', yml_views.list, name='list'), 
    url(r'^$', yml_views.index),
    url(r'^map/', yml_views.map),
    url(r'^bashroom/', yml_views.bashroom),
    url(r'^activity/', yml_views.activity),
    url(r'^canteen/', yml_views.canteen),
    url(r'^list/spot/(\d+)/$', yml_views.item, name='item'),
]
