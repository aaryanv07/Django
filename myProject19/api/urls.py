from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token #used to display the token of user
from .import views
'''
urlpatterns=[
    path('public/',views.public_view,name='public'),
    path('private/',views.private_view,name='private'),
]'''

'''
urlpatterns=[
    path('',views.blog_list,name='blog_list'),

]
'''
urlpatterns=[
    path('auth-token/',obtain_auth_token,name='auth_token'),
    path('profile/',views.user_profile,name='profile'),
    path('admin-panel/',views.admin_panel,name='admin_panel'),

]