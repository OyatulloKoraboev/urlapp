from django.contrib import admin
from django.urls import path
from .views import contacts
urlpatterns = [
    path('',contacts, name='contact'),
]
