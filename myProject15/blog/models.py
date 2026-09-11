from django.db import models
from django.urls import reverse # used for giving the absolute path

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    # date_posted = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self): # Will be run after every view
        return reverse('post_detail', args = [str(self.id)])
        