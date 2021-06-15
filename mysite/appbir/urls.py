
from django.contrib import admin
from django.urls import path
from .views import home, about, contacts
urlpatterns = [
    path('', home, name='appbir_home'),
    path('appuch/', about, name='appbir_about'),
    path('appikki/', contacts, name='appbir_about'),
]
