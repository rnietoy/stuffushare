from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from user.forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout

class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return HttpResponseRedirect('/doesnotexist')

        authUser = authenticate(username=user.username, password=password)
        if authUser is not None:
            if authUser.is_active:
                login(self.request, authUser)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/error')
        else:
            return HttpResponseRedirect('/invalid')

class RegisterView(FormView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        new_user = User.objects.create_user(form.cleaned_data['email'], 
            form.cleaned_data['email'],
            form.cleaned_data['password'],
            )
        new_user.first_name = form.cleaned_data['name']
        new_user.save()

        authUser = authenticate(username=new_user.username, password=form.cleaned_data['password'])
        login(self.request, authUser)
        return HttpResponseRedirect('/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')