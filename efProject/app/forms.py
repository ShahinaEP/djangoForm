from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class':'form-control my-2',
        'placeholder':'Enter your Name'
    }))

    email = forms.EmailField(max_length=150, widget=forms.EmailInput(attrs={
        'class':'form-control my2',
        'placeholder':'email@gmail.com'
    }))

    phone = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class':'form-control my-2',
        'placeholder':'Enter your phone'
    }))

    message = forms.CharField(max_length=150, widget=forms.Textarea(attrs={
        'class':'form-control my-2',
        'placeholder':'Enter your phone',
        'rows':3
    }))

    #  = models.EmailField()
    #  = models.CharField(max_length=150)
    # message = models.TextField()
    class Meta:
        model = Contact
        fields =['name', 'email', 'phone', 'message']

class ContactForm2(forms.ModelForm):
    class Meta:
        model = Contact
        fields ='__all__'
