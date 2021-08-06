from django.shortcuts import render
from .forms import *
from .models import *

from django.contrib.auth.models import *
from django.contrib.auth.models import User




def register(request):

    if request.method == 'POST':
        user_form = usersmodelregisterform(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)

            u = User.objects.get(username = new_user.username)
            u.set_password()
            u.save()
            
            new_user.set_password(user_form.cleaned_data['userpassword1'])
            
            new_user.save()
            return render(request, 'users/register_done.html', {'new_user': new_user})
    else:
        user_form = usersmodelregisterform(request.POST)
        return render(request, 'users/register.html', {'user_form': user_form})


def index(request):
    return render(request, 'users/index.html')


def example(request):
    b_model = blogmodel.objects.all()
    uno_model = blogmodel(blogname='Anton')

    dos_model = blogmodel.objects.get(blogname='Egor')
    


    a = {
        'b_model': b_model,
        'uno_model' : uno_model,
        'dos_model': dos_model,
    }

    return render(request, 'users/all.html', a)