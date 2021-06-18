from .models import usersmodel
from django import forms


class usersmodelregisterform(forms.ModelForm):
    password1 = forms.CharField(label=' first Password ', widget=forms.PasswordInput)
    password2 = forms.CharField(label=' second Password ', widget=forms.PasswordInput)

    class Meta:
        model = usersmodel
        fields = ('username', 'usermail', 'userpassword1', 'userpassword2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']