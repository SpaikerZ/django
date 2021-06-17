from django import forms
from .models import postmodel

class postform(forms.ModelForm):

    NamePost = forms.CharField(max_length = 100)

    class Meta:

        fields = ('NamePost', 'TextPost', 'ConfirmId' )
        model = postmodel


class inputidform(forms.ModelForm):

    ConfirmId = forms.CharField( max_length = 15)

    
    class Meta:
        ConfirmId = forms.CharField(max_length = 15)
        fields = ('ConfirmId',)
        model = postmodel

"""
         your_id = forms.CharField(label='Your id', max_length=100)
  def clean(self):
     cleaned_data = super(NameForm, self).clean()
     your_id = cleaned_data.get("your_id")
     p = UserInfo.objects.all()
     if your_id:
        for i in p:
           if i.usrId not in your_id:
              raise forms.ValidationError(
                   "User not exist."
                  )
                  """