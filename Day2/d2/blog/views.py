from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>This is from views.py</h1>")

def about(request):
    a=21
    return HttpResponse(f'<h1>You are forever {a}</h1>')

