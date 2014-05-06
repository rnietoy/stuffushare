from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name="base.html"

    def get_context_data(self, **kwargs):
        return {'user_name': "Angel"}