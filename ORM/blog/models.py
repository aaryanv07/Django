from enum import unique
from django.db import models

# Create your models here.
class Student(models.Model): # name of the class is the name of the table
    #fields
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    # enrollment_date = models.DateField(auto_now_add=True)
    city=models.CharField(max_length=100,default=None)
      
    def __str__(self):
        return self.name

# Migrate the above 
# 1. python3 manage.py makemigrations (generates sql)

# Creates a file in migrations folder
# 2. python3 manage.py migrate  (apply sql) --> will be visible in .sqlite3 file
# install sqlite3 editor extension

#  For making changes in the Data defination (structure) --> run makemigrations and migrate 

# shell commands in django interactive mode --> python3 manage.py shell
 
# inserting the data manually in .dbsqlite3 file

# from blog.models import Student
# s1 = Student.objects.all() --> will return all objects of the model in a queryset 
# s1
# print (s1)--> will return all the query set

# for loop in shell for s in s1:
#   print(s.name,s.age,s.city)


# Using of get() only on unique items 
# s1=Student.objects.get(city="Punjab")
# s1
# By default name is getting executed  | anything else can be get through s1.age

# Using of filter()
# s1=Student.objects.filter(city="Punjab")
# s1
# s1=Student.objects.filter(age__gt=30)
# s1
# s1=Student.objects.filter(name__startswith="a")
# s1

# * Ordering & Chaining
# from blog.models import Student
# students = Student.objects.all().order_by('name')
# students = Student.objects.all().order_by('age') (Ascending order)
# students = Student.objects.all().order_by('-age') (Ascending order)
# students = Student.objects.all().order_by('city','-age') (Ascending order)

# Filter chaining (Chaining of multiple filters)
# s1=Student.objects.filter(age__gt=30).filter(city="Pune").order_by('name')


# Exclude (Excluding the value)
# s1=Student.objects.exclude(name__startswith="a")


# values() (returning the value in dict format)
# values("name")
# s1=Student.objects.values("name","age")
# s1=Student.objects.values_list("name","age")
# s1=Student.objects.values_list("name",flat=True) ( Easily convert to a standard Python list if needed:)

# first and last and count
# s1=Student.objects.first()
# s1=Student.objects.last()
# s1=Student.objects.count()