from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class List(TemplateView):
    template_name = "frontend/list.html"