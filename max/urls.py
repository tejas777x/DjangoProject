from django.urls import path
from . import views
from django.urls import path, include
from django.conf.urls import url

app_name = 'max'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),  # url to load register function
    url(r'^user_login/$', views.user_login, name='user_login'),  # url to call login page
    path(r'^/Electronics/(?P<id>)/$', views.Electronics, name="populate"),  # url to call Electronics module
    path(r'^/Seller/(?P<id>)/$', views.Seller, name="populate"),  # url to call Seller module
    path(r'^ajax/load-electronics/', views.load_electronics, name='ajax_load_electronics'),  # url for ajax call to call load_electronics function
    path(r'^ajax/load-seller/', views.load_seller, name='ajax_load_seller'),  # url for ajax call to call load_seller function
    path(r'^ajax/load_list/', views.load_list, name='ajax_load_list'), # url for ajax call to call load_list function
    path(r'^ajax/subscribe/', views.subscribe, name='ajax_subscribe'), # url for ajax call to call subscribe function
]
