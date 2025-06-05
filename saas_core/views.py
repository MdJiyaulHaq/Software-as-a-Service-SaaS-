from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

def home_view(request):
    return render(request, 'home.html')
