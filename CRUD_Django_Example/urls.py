"""CRUD_Django_Example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from CRUD_FBVs import views

app_name = 'CRUD_FBVs'

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.movies_list, name='movies_list'),
    url(r'^new$', views.movies_create, name='movies_new'),
    url(r'^edit/(?P<pk>\d+)$', views.movies_update, name='movies_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.movies_delete, name='movies_delete'),
]
