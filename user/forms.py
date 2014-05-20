from django import forms

class LoginForm (forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

class RegisterForm (forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    name = forms.CharField()