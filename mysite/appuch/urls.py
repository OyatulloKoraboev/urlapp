from django.contrib import admin
from django.urls import path
from .views import about,home,contacts
urlpatterns = [
    path('', home, name='appuch_home'),
    path('about/', about, name='appuch_about'),
    path('contacts/', contacts, name='appuch_about'),
]
