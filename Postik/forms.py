from django import forms
from .models import *

class postform(forms.ModelForm):

    NamePost = forms.CharField(max_length = 100)

    class Meta:

        fields = ('NamePost', 'TextPost', 'ConfirmId' )
        model = postmodel



class inputidform(forms.ModelForm):

    ConfirmId = forms.CharField( max_length = 15)

    
    class Meta:
        
        fields = ('ConfirmId',)
        model = confirmmodel

