# Generated by Django 5.1.5 on 2025-01-20 17:40

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_room_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.uuid1, unique=True),
        ),
    ]
