# Generated by Django 5.0.4 on 2024-08-18 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0016_alter_event_time_alter_project_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='crcclass',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to='classes/images'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to='events/images'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=4096, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to='projects/images'),
        ),
        migrations.AlterField(
            model_name='project',
            name='summary',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
