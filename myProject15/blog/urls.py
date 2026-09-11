
from django.urls import path
from .views import PostListView , PostDetailView,PostCreateView,PostUpdateView,PostDeleteView

urlpatterns=[path('',PostListView.as_view(),name='post_list'),
path('post/<int:pk>/',PostDetailView.as_view(),name='post_detail'),  # pass the id int the int
path('post/new/',PostCreateView.as_view(),name='post_create'), # pass the id int the int
path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post_update'), # pass the id int the int
path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post_delete') # pass the id int the int
]

