from django import forms
from django.contrib.auth.models import User
from . import models
from .models import User,Customer  




class CustomerUserForm(forms.ModelForm):
    class Meta:
        model = UserWarning
        fields =['first_name','list_name','username','password']
        widgets ={
            'password': forms.passwordInput()
        }
        class CustomerForm(forms.ModelForm):
            class Meta:
                model = Customer 
                fields = ['address','mobile','profile_pic']