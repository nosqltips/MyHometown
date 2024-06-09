from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    time = models.DateTimeField(default=timezone.now)
    url = models.CharField(max_length=255, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    description = models.CharField('Description of the event', max_length=4096, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})
  
class Class(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    times = models.CharField(max_length=255)
    date_posted = models.DateTimeField(default=timezone.now)
    description = models.CharField('Description of the class', max_length=4096, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('class-detail', kwargs={'pk': self.pk})

class Project(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    time = models.DateTimeField(default=timezone.now)
    url = models.CharField(max_length=255, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    description = models.CharField('Description of the project', max_length=4096, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})
