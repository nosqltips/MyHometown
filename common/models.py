from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit
from imagekit.forms import ProcessedImageField


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    time =models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    url = models.CharField(max_length=255, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    summary = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=4096, null=True)
    image_file = models.ImageField(upload_to='events/images', null=True, blank=True)
    image = ImageSpecField(source='image_file',
                                processors=[ResizeToFit(1024, 768)],
                                format='JPEG',
                                options={'quality': 60})
    is_private = models.BooleanField(default=False)
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
    description = models.TextField(max_length=4096, null=True)
    image_file = models.ImageField(upload_to='classes/images', null=True, blank=True)
    image = ImageSpecField(source='image_file',
                                processors=[ResizeToFit(1024, 768)],
                                format='JPEG',
                                options={'quality': 60})
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('crcclass-detail', kwargs={'pk': self.pk})
    
class CRCRegister(models.Model):
    crcclass = models.ForeignKey(CRCClass, related_name='registrations', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('crcclass-detail', kwargs={'pk': self.pk})

class Project(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    time = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    url = models.CharField(max_length=255, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    summary = models.CharField(max_length=255, null=True )
    description = models.TextField(max_length=4096, null=True)
    image_file = models.ImageField(upload_to='projects/images', null=True, blank=True)
    image = ImageSpecField(source='image_file',
                                processors=[ResizeToFit(1024, 768)],
                                format='JPEG',
                                options={'quality': 60})
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})

class TimeTrack(models.Model):
    location = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)
    date_posted = models.DateTimeField(default=timezone.now)
    crc = models.FloatField(null=True, blank=True)
    service = models.FloatField(null=True, blank=True)
    other = models.FloatField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('time-list')