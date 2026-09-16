from django.urls import path,include
# from .views import StudentAPI
# from .views import StudentListCreateAPI,StudentRetriveUpdateDeleteAPI
from rest_framework.routers import DefaultRouter

from .views import StudentModelViewset





'''
urlpatterns = [
    path('', StudentAPI.as_view()),
    path('<int:id>/', StudentAPI.as_view()),
]

'''
'''
urlpatterns=[
    path('student/',StudentListCreateAPI.as_view()),
    path('student/<int:pk>/',StudentRetriveUpdateDeleteAPI.as_view()),
]

'''
router =DefaultRouter()
router.register('students',StudentModelViewset,basename='student')

urlpatterns = router.urls
# run the project
# http://127.0.0.1:8000/students/ # Get All students data
# http://127.0.0.1:8000/students/1/ # Get single student data
# http://127.0.0.1:8000/students/4/ # Delete student data'''

