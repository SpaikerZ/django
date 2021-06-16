from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'Postik/index.html')

def create(request):
    return render(request, 'Postik/create.html')

def see(request):
    return render(request, 'Postik/see.html')

def change(request):
    return render(request, 'Postik/change.html')

def remove(request):
    return render(request, 'Postik/remove.html')