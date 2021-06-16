from django import forms
from .models import postmodel

class postform(forms.ModelForm):

    NamePost = forms.CharField(max_length = 15)

    class Meta:

        fields = ('NamePost', 'TextPost', 'ConfirmId' )
        model = postmodel