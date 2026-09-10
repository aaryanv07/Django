from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    city=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Profile(models.Model):
    bio=models.TextField()
    location=models.CharField(max_length=100)
    birth_date=models.DateField(null=True,blank=True)

   

# python3 manage.py makemigrations (RUNS on all the installed apps)
# python3 manage.py migrate (RUNS on all the installed apps)