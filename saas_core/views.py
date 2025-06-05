from django.http import HttpResponse
from django.urls import path

def home_view(request):
    return HttpResponse("Hello World!")
