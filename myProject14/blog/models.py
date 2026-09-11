from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    category=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.title # Data will be represented by the title in admin panel

# run makemigrations and migrate to update the database
# python manage.py makemigrations
# python manage.py migrate

# Create superuser -- admin -- admin@gmail.com -- admin