from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    url = models.CharField(max_length=255, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    description = models.CharField('Description of the event', max_length=4096, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

    # This actually needs to go to private
    def get_absolute_url(self):
        return reverse('public-event-detail', kwargs={'pk': self.pk})
  