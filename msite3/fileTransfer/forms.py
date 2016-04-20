from django import forms
# from .models import User
from django.contrib.auth.models import User
from .models import UserProfile
from django.db import models
from django.forms import ModelForm
from django.core.context_processors import csrf


# class UserForm(ModelForm):
#     class Meta:
#         model=User
#         fields=['name', 'password', 'ip_address', 'file_directory','friends']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website',)

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )
