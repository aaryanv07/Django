from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    # email=models.EmailField()
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def _str__(self):
        return self.name 

# python3 manage.py makemigrations contact
# python3 manage.py migrate
    