from django.db import models
from django.utils import timezone
# Create your models here.

class Post_model(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    author = models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    

    
