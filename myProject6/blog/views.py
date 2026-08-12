from django.shortcuts import render
from datetime import datetime
# Create your views here.
post={'title':"My second Templates Post",
"descriptions":"Django is is a high-level Python web framework That encourages rapid development and clean, pragmatic design.",
'author':None,
'created_at':datetime(2026,8,18,10,30),
'comments_count':5,
'tags':['python','django','web_framework']
}
def blog_details(request):
    return render(request,"blog/blog_details.html",{'post':post})