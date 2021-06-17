
from django.contrib import admin
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Postik.urls')),
    #path('', include("createPost.urls")) see settings.py
]
