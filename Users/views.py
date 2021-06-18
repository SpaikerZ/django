from django.shortcuts import render
from .forms import *



def register(request):

    if request.method == 'POST':
        user_form = usersmodelregisterform(request.POST)

        if user_form.is_valid():
            newuser = user_form.save(commit=False)

            new_user.set_password(user_form.cleaned_data['password1'])
            
            new_user.save()
            return render(request, 'users/register_done.html', {'new_user': new_user})
    else:
        user_form = usersmodelregisterform()
    return render(request, 'users/register.html', {'user_form': user_form})

def index(request):
    return render(request, 'users/index.html')