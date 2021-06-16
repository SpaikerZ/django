from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from . import models

# Create your views here.

def index(request):
    return render(request, 'Postik/index.html')

def create(request):
    
    if request.method == 'POST':
        form = createFrom(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.save()

            return render(request, 'Postik/index.html')
        
        else:
            return HttpResponse("<h1>Form not valid </h1><h2>Or something was wrong</h2>")
    
    return render(request, 'Postik/create.html')
















def see(request):
    return render(request, 'Postik/see.html')

def change(request):
    return render(request, 'Postik/change.html')

def remove(request):
    return render(request, 'Postik/remove.html')