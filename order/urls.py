from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^restaurants/$', views.restaurant_list, name='restaurant_list'),
    url(r'^restaurants/(?P<pk>[0-9]+)/$', views.menu, name = 'menu'),
]
