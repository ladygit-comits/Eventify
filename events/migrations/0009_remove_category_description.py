# Generated by Django 4.2.16 on 2024-12-09 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_event_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
    ]
