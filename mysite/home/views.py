from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('Home Page View')
