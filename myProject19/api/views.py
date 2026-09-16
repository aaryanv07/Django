from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token


# Create your views here.
# Public view accessible without authentication

'''
@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    return Response({'message':'This is a public view'})

# Private view accessible only by authenticated users
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def private_view(request):
    return Response({'message':f'Hello, {request.user.username} This is a private view'})
'''
# Run the commands python manage.py makemigrations && python manage.py migrate
# create superuser python manage.py createsuperuser 
# admin ,admin,admin@gmail.com

# Run the server 
# python manage.py runserver

# http://127.0.0.1:8000/public/ (public view)
# http://127.0.0.1:8000/private/ (private view)

# Enter the user ceredentials created above to authenticate


'''
#Session Authentication
@api_view(['GET','POST'])
def blog_list(request):
    if request.method =='GET':
        blogs=Blog.objects.all()
        serializer = BlogSerializer(blogs,many=True)
        return Response(serializer.data)
    if request.method =='POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        '''
        
# Run the server
# use liteclient for testing the post endpoint
# {
#   "detail": "Authentication credentials were not provided."
# }

# login through the admin panel

# post method will work on browser as it saves your data --> browser handles CSRF and tokens

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user=request.user
    return Response({'user':user.username,'email':user.email,"is_staff":user.is_staff,"is_superuser":user.is_superuser})



#api Only for admin users

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def admin_panel(request):
    return Response({'message':f'welcome to the admin panel {request.user.username}'})

# run the server

# and test the endpoints on lite client
# /auth-token/ --> returns the token for user


# new request --> method = Post (data needs to be sent as method is POST)--> body --> raw tab -->  {"username":"admin","password":"admin"}

# copy the  token --> "8971c8f6f5a8f75e8deb03ccbce4ac314d383a06"

# change the request to get and add this in the header --> key: Authorization Value: Token 8971c8f6f5a8f75e8deb03ccbce4ac314d383a06

# DO the same for the admin-panel

# Normal user token cannot access the admin data