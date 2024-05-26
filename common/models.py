from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    time = models.DateTimeField(default=timezone.now)
    description = models.TextField
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
  