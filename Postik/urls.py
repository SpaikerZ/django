
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from . import views

urlpatterns = [
    path('', views.index ),
    path('create_post/', views.create ),
    path('see_posts/', views.see ),
    path('change_post/', views.change ),
    path('remove_post/', views.remove ),
    
    #path('postik/', include('Postik.urls')),
    #path('', include("createPost.urls")) see settings.py
]
