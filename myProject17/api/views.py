from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

# Create your views here.

# Works for getting the data from the model.
@api_view(['GET'])
def student_list(request):
    student_list=Student.objects.all()
    serializer=StudentSerializer(student_list,many=True) # Convert complex data(QuerySet) to JSON $
    # many=True tell that data set has multiple field i.e name.age etc (QuerySet)
    
    return Response(serializer.data) # Response object serializes the data and returns it as JSON

@api_view(['POST'])
def add_student(request):
    serializer=StudentSerializer(data=request.data) # Convert complex data(QuerySet) to JSON $
    if serializer.is_valid(): # Check if the data is valid
        serializer.save() # Save the data
        return Response(serializer.data,status=status.HTTP_201_CREATED) # Response object serializes the data and returns it as JSON
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) # Return the errors if the data is not valid

@api_view(['PUT','PATCH'])
def updated_student(request,id):
    try:
        student=Student.objects.get(id=id) 
    except Student.DoesNotExist:
        return Response({'errors':'Student not found'},status=status.HTTP_404_NOT_FOUND)

    # Partial api support
    if request.method=='PATCH':
        serializer=StudentSerializer(student,data=request.data,partial=True)
       
    else:
        serializer=StudentSerializer(student,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_student(request,id):
    try:
        student=Student.objects.get(id=id) 
    except Student.DoesNotExist:
        return Response({'errors':'Student not found'},status=status.HTTP_404_NOT_FOUND)
    student.delete()
    return Response({'Status':'Student deleted'},status=status.HTTP_200_OK)
    