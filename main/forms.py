from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        help_texts = {
            'username': None,
            'email':None,
            'password1': 'good pa',
            'password2': None,
        }
   
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
       

        self.fields['password1'].label='password'
        self.fields['password1'].help_text=''
  
        
        self.fields['password2'].label='re-enter password'
        self.fields['password2'].help_text=''