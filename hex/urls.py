from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from max import views

from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls), # url to load the site
    url(r'^$', views.index, name='index'),  # url to load index function
    url(r'^max/', include('max.urls')), # url to include urls present in max\urls.py
    url(r'^database/', views.test, name='database'),  # url to load test function
    url(r'^special/', views.special, name='special'),  # url to load special function
    url(r'^logout/$', views.user_logout, name='logout'),  # url to call logout page
    path('ajax/load-electronics/', views.load_electronics, name='ajax_load_electronics'),  # url for ajax call to call load_electronics function
    path('ajax/load-seller/', views.load_seller, name='ajax_load_seller'),  # url for ajax call to call load_seller function
    path('ajax/load_list/', views.load_list, name='ajax_load_list'),  # url for ajax call to call load_list function
    path('ajax/subscribe/', views.subscribe, name='ajax_subscribe'),   # url for ajax call to call subscribe function
]
