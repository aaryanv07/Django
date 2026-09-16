from django.urls import path
from .import views
urlpatterns = [
    path('student/', views.student_list),
    path('student/add/', views.add_student),
    path('student/update/<int:id>/', views.updated_student),
    path('student/delete/<int:id>/', views.delete_student),
]