from django.contrib.auth.models import User
from django import forms 
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    email = forms.EmailField(max_length=100, widget = forms.EmailInput(attrs = {'class': 'form-control'}))
    
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')