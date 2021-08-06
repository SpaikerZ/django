
from Postik.views import index
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('postik/', include('Postik.urls')),
    path('users/', include('Users.urls')),
    #path('', include("createPost.urls")) see settings.py
    path('', views.index)
]
