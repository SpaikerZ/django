from django.shortcuts import render
from django.http import HttpResponse
from .forms import postform
from .models import postmodel

# Create your views here.

def index(request):
    return render(request, 'Postik/index.html')

def create(request):
    
    if request.method == 'POST':
        form = postform(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.save()

            allPosts = postmodel.objects.all()
            return render(request, 'Postik/see.html', {'allPosts':allPosts})
        
        elif form.is_valid() == False:
            return HttpResponse("<h1>Form not valid </h1><h2>Or something was wrong</h2>")

        else:
            return HttpResponse("<h1>Form not valid </h1><h2>Or something was wrong</h2>")
    
    
    return render(request, 'Postik/create.html')




def see(request):
    allPosts = postmodel.objects.all()
    
    a = 0
    for i in allPosts:
        a += 1
    allPostsLen = a
    
    return render(request, 'Postik/see.html', {'allPosts':allPosts})






def change(request):
    return render(request, 'Postik/change.html')

def remove(request):
    return render(request, 'Postik/remove.html')