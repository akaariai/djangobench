from django.conf.urls import *

urlpatterns = patterns('default_middleware',
    (r'^.*$', 'views.index'),
)
