from django.shortcuts import render
from datetime import datetime
# Create your views here.
post={'title':"My second Templates Post",
"description":"Django is is a high-level Python web framework That encourages rapid development and clean, pragmatic design.",
'author':None,
'created_at':datetime(2026,8,18,12,30),
'comments_count':5,
'tags':['python','django','web_framework'],
'price':100.4567,
'number':7
}
def blog_details(request):
    return render(request,"blog/blog_details.html",{'post':post})