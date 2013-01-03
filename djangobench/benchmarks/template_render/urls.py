from django.conf.urls import *

urlpatterns = patterns('template_render.views',
    url(r'/join/?$', 'join', name='join'),
    url(r'/login/?$', 'login', name='login'),
    url(r'/logout/?$', 'logout', name='logout'),
)
