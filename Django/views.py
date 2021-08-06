from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<p><a href ='postik/'><button>postik</button></a></p> <p><a href ='users/'><button>users</button></a></p>")