from socket import fromshare
from django.core import validators
from django import forms
from matplotlib import widgets
from.models import User
from xmlrpc.client import DateTime

class EmployeeRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','role','salary','city','dob']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'role': forms.TextInput(attrs={'class':'form-control'}),
            'salary': forms.NumberInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={'class':'form-control','type':'date'}),
    
        }