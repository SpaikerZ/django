from .models import usersmodel
from django import forms

from django.contrib.auth.models import User


class usersmodelregisterform(forms.ModelForm):
    userpassword1 = forms.CharField(label=' first Password ', widget=forms.PasswordInput)
    userpassword2 = forms.CharField(label=' second Password ', widget=forms.PasswordInput)
    username = forms.CharField(max_length=64)
    class Meta:
        model = usersmodel
        fields = ('username', 'usermail', 'userpassword1', 'userpassword2')
    
    def set_password(self):
    #def clean_password2(self):
        cd = self.cleaned_data
        if cd['userpassword1'] != cd['userpassword2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']