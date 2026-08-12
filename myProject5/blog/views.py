from django.shortcuts import render
from datetime import datetime
# Create your views here.
class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age
def home(request):
    context={'name':"Mohit Kumar",
    'age':25,
    'skills':['Python','Django','SQL'],
    'user':User('Kumar',30),
    'blog':{'title':'My First Blog Post',
    'author':{'name':'Kumar','age':30},
    'content':'<b>This is the content of my first blog post</b>',
    'created_at':datetime(2026,8,18,10,30)},
    'empty_value':None,}    

    return render(request,'blog/home.html',context)
    