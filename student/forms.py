from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Enter Admission Number...', 'class': 'input-field-box'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password...', 'class': 'input-field-box'}))