from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    city=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# python3 manage.py makemigrations students
# python3 manage.py migrate 
# python3 manage.py runserver 