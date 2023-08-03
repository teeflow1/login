from django.contrib.auth.models import User
from blog.models import Able
from django import forms





class UserAddForm(forms.ModelForm):
    
    name=forms.CharField( required = True, max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    price= forms.CharField( required = True, max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    address=forms.CharField( required = True, max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    '''
    country=forms.CharField( required = True, max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    state=forms.CharField( required = True, max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    city=forms.CharField( required = True, max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    email=forms.CharField( required = True, max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    phone_no=forms.CharField( required = True, max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    
    '''
    class Meta:
        model = Able
        #exclude = ("user",)
        fields = ('name', 'price', 'address')
    