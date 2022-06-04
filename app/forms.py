from django import forms
from django.forms.widgets import Textarea
from .models import *
from django.contrib.auth.forms import UserCreationForm

class SettingsForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    avatar = forms.ImageField()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class QuestionForm(forms.ModelForm):
    tags = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'tags...'}))
    text =  forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Question
        fields = ['title', 'text']



class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    avatar = forms.ImageField()




