from django.db import models
from django.utils import timezone
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    profile_picture_thumbnail = ImageSpecField(source='profile_picture',
                                              processors=[ResizeToFill(100, 100)],
                                              format='JPEG',
                                              options={'quality': 60})
    is_missionary = models.BooleanField(default=False)

    def get_profile_picture(self):
        if self.profile_picture:
            return self.profile_picture.url
        # or any other default image
        return '/static/default_profile_picture.png'
    
    def get_profile_picture_thumbnail(self):
        if self.profile_picture:
            return self.profile_picture_thumbnail.url
        # or any other default image
        return '/static/default_profile_thumbnail_pic.png.png'
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
 
class TimeLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.FloatField

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'