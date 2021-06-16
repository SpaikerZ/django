from django import forms
from .models import postmodel

class postform(forms.ModelForm):

    class Meta:

        fields = ('NamePost', 'TextPost', 'ConfirmId' )
        model = postmodel