from django import forms
from .models import User
from django.db import models
from django.forms import ModelForm
from django.core.context_processors import csrf


class UserForm(ModelForm):
    class Meta:
        model=User
        fields=['name', 'password',]
