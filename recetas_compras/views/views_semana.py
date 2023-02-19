from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse('Hola Mundo')

class Home(TemplateView):
    template_name = "home.html"

