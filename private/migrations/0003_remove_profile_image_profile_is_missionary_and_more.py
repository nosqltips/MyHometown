# Generated by Django 5.0.4 on 2024-08-05 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('private', '0002_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.AddField(
            model_name='profile',
            name='is_missionary',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile_pictures'),
        ),
    ]
