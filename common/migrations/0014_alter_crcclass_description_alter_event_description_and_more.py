# Generated by Django 5.0.4 on 2024-08-17 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0013_alter_crcclass_description_alter_event_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crcclass',
            name='description',
            field=models.TextField(max_length=4096, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=4096, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, max_length=4096, null=True),
        ),
    ]