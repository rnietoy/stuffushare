from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Welcome to StuffUShare!")
