from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *

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
    countPosts = len(list(allPosts))
   
    allPostslist = {
        'allPosts': allPosts,
        'countPosts': countPosts

    }

    return render(request, 'Postik/see.html', allPostslist)



def change(request):
    return HttpResponse('<h1>This `{}` </h1>'.format(postmodel.objects.all()))
    
    """
    Qpostmodels = postmodel.objects.all()
    catmodels = postmodel.objects
    if request.method == 'POST':
        form_id = inputidform(request.POST)

        if form_id.is_valid():
            task = form_id.save(commit=False)
            task.save()
            conf = confirmmodel.ConfirmId[0] 
            #if conf in Qpostmodels.get(ConfirmId=conf):
            if catmodels.filter(ConfirmId__startswith=conf):    
                return HttpResponse("<h1>Succes</h1>")
            else:
                return HttpResponse("<h1>Form is only save</h1>")
        else:
            return HttpResponse("<h1>Form not valid</h1>")

    else:
        return render(request, 'Postik/confirm.html', {'Qpostmodels':Qpostmodels})
"""



def remove(request):
    return render(request, 'Postik/remove.html', )