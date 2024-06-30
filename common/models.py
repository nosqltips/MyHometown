from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    time = models.TimeField(default=timezone.now)
    date = models.DateField(default=timezone.now)
    url = models.CharField(max_length=255, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    summary = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=4096, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})
  
class CRCClass(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    times = models.CharField(max_length=255)
    date_posted = models.DateTimeField(default=timezone.now)
    summary = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=4096, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('class-detail', kwargs={'pk': self.pk})
    
class Signup(models.Model):
    crcclass = models.ForeignKey(CRCClass, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('class-detail', kwargs={'pk': self.pk})

class Project(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    time = models.TimeField(default=timezone.now)
    date = models.DateField(default=timezone.now)
    url = models.CharField(max_length=255, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    summary = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=4096, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})
