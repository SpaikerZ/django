
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from . import views

urlpatterns = [
    path('', views.index ),
    path('create_post/', views.create, name='creating' ),
    #path('see_posts/', views.see ),

    path('see_posts/', views.SeeListView.as_view(), name='See'),

    path('change_post/', views.change, name='changing' ),
    path('remove_post/', views.remove, name='removing' ),
    
    #path('postik/', include('Postik.urls')),
    #path('', include("createPost.urls")) see settings.py
]
