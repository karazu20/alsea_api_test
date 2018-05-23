from django.conf.urls import url
from api import views


urlpatterns = [ 
    url(r'^elementos/$', views.elem_list),
    url(r'^elementos/(?P<pk>\d+)/$', views.elem_get), 
]