from django.template import context # This line imports Django’s Context class,
# which is used to pass data into a template.
from django.shortcuts import render
from datetime import datetime
import pytz


# Create your views here.
def blog_details(request):
    ist = pytz.timezone("Asia/Kolkata")
    ist2 = datetime.now()
    blogs=[
        {'title':"django basics",'is_featured':True,'author':'Mohit Kumar'},
        {'title':'django Advanced','is_featured':False,'author':'John Doe'},
        {'title':'django REST Framework','is_featured':True,'author':'Jane'}]

    context={'blogs':blogs,
    'today':datetime.now(ist),
    'today(normal)':ist2,
    'html_code':'<h1>Welcome to my Blog</h1>',
               }
    return render(request,'blog/blog_list.html',context)
