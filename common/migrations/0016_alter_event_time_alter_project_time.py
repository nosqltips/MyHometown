# Generated by Django 5.0.4 on 2024-08-18 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0015_crcclass_image_file_event_image_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='time',
            field=models.CharField(max_length=100),
        ),
    ]
