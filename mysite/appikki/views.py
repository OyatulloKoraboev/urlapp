from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('Home Page View')


def about(request):
    return HttpResponse('About Page View')


def contacts(request):
    return HttpResponse('Contacts Page View')
