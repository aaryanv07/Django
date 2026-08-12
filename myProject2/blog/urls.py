
from django.urls import path,re_path
from . import views

urlpatterns=[
    path('post/<int:post_id>/',views.post_details,name='post_details'),
    path('user/<str:username>/',views.user_profile,name='user_profile'),
    re_path(r'^article/(?P<year>[0-9]{4})/$',views.articles_by_year,name='articles_by_year'),
    path('article/<int:year>/<int:month>/<int:day>/',views.article_details,name='article_details')
    ]


# http://127.0.0.1:8000/blog/article/2025/04/5/