# Generated by Django 4.2.16 on 2024-12-07 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_delete_imagemodel_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
