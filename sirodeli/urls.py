# -*- coding: utf-8 -*-
"""sirodeli URL Configuration

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
from django.contrib import admin

from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static # относится к ckeditor
from django.conf import settings # относится к ckeditor
#from sirodeli1.views import index

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('userprof.urls', namespace='userprofname')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^', include('sirodeli1.urls', namespace='sirodeli1name')),
    #url(r'^$', index), #передача нужных параметров на все страницы из sirodeli1.views
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

