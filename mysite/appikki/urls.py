from django.contrib import admin
from django.urls import path
from .views import contacts, home, about
urlpatterns = [
    path('', home, name='appbir_home'),
    path('about/', about, name='appbir_about'),
    path('contacts/', contacts, name='appbir_about'),
]
