from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return "f'{self.user.first_name}, {self.user.last_name}'"
 
class TimeLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.FloatField

    def __str__(self):
        return "f'{self.user.first_name}, {self.user.last_name}'"