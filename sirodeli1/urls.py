# -*- coding: utf-8 -*-
from django.conf.urls import url,include,patterns
from django.conf import settings
from django.conf.urls.static import static
from sirodeli1 import views

urlpatterns = [
    #url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^$', 'sirodeli1.views.demo_func', name='post_all'),
    url(r'^add/$', 'sirodeli1.views.my_form', name='post_add'),
    url(r'^(?P<pk>[0-9]+)/$', 'sirodeli1.views.post_detail', name='post_details'),
    url(r'^delete/(?P<pk>[0-9]+)/$', 'sirodeli1.views.delete_new', name='post_del'),

    #delete_new
]#+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#if settings.DEBUG:
#    urlpatterns += patterns('',
#                        # myguest:
#                        (r'^ckeditor/', include('ckeditor.urls')),
#
#                        ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
#    )
