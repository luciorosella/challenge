from django.contrib import admin
from django.urls import path

# IMPORT CUSTOMS
from challenge.views import hello_geek

urlpatterns = [
    path('vwamp/', hello_geek), 
]
