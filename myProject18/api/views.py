from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from .models import Student
from .serializers import StudentSerialzer
from rest_framework import generics,mixins
# CRUD operation APIView 

# Create your views here.
'''
class StudentAPI(APIView):
    # getting the data
    def get(self,request,id=None):
        # single data
        if id:
            try:
              student = Student.objects.get(id=id)
              s=StudentSerialzer(student)
              return Response(s.data,status=status.HTTP_200_OK)
            except: return Response({"error":"Student not found"})

        else:
            # many data

          s=StudentSerialzer(Student.objects.all(),many=True)
          return Response(s.data,status=status.HTTP_200_OK)

    
    # creating the data
    def post(self,request):
      serializer=StudentSerialzer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # Update the data (PUT)
    def put(self,request,id):
        try:
            student = Student.objects.get(id=id)
            serializer = StudentSerialzer(student,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except: return Response({"error":"Student not found"})

    # delete the data (DELETE)
    def delete(self,request,id):
        try:
            student = Student.objects.get(id=id)
            student.delete()
            return Response({"message":"Student deleted successfully"},status=status.HTTP_200_OK)
        except: return Response({"error":"Student not found"})


'''
'''
# CRUD operation GenricAPIView + mixins
class StudentListCreateAPI(generics.GenericAPIView #base class of Django Rest Framework for defining query set and serializer class
,mixins.ListModelMixin,mixins.CreateModelMixin):
# Mixins are pre build classes where logic of CRUD operatins is written):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer

    #Read all data (Works as get api) | Get endpoint
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    #Create data (Works as post api) | Post endpoint
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class StudentRetriveUpdateDeleteAPI(generics.GenericAPIView
,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
  queryset = Student.objects.all()
  serializer_class = StudentSerialzer

    #get single data
  def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    # Update the data (PUT)
  def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    # delete the data (DELETE)
  def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

'''
# FULL CRUD using modelviewset + router
class StudentModelViewset(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerialzer

  #five build in methods -->
#   list(),retrieve(),create(),update(),partial_update(),destroy()

        






        
          
        
    
