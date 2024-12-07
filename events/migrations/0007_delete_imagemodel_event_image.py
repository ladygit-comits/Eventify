# Generated by Django 4.2.17 on 2024-12-07 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_imagemodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ImageModel',
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]