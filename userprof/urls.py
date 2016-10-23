# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from userprof import views

urlpatterns = [
	#url(r'^$', 'sirodeli1.views.demo_func', name='post_all'),
    url(r'^login/$', 'userprof.views.login', name='login'),
	url(r'^logout/$', 'userprof.views.user_logout', name='logout'),
	url(r'^$', 'userprof.views.user', name='userurl'),
]