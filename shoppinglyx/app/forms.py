from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm , UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext , gettext_lazy as _

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', max_length=150,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', max_length=150,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=150,widget=forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class': 'form-control'}))
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(attrs=
                        {'autocomplete':'current-password','class': 'form-control'}))



