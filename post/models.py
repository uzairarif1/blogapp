from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    description= models.CharField(max_length=500)
    created_time = models.DateTimeField(default=datetime.now,blank=True)
