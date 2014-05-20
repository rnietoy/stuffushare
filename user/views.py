from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from user.forms import LoginForm, RegisterForm

class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
    	return HttpResponseRedirect('/')

class RegisterView(FormView):
	template_name = "register.html"
	form_class = RegisterForm
	success_url = '/'

	def form_valid(self, form):
		new_user = User.objects.create_user(form.cleaned_data['email'],
			form.cleaned_data['password'],
			form.cleaned_data['name'])
		new_user.save()
		return HttpResponseRedirect('/')