from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello World</h1>")
def about(request):
    a=21
    return HttpResponse(f"You are forever {a}")