# Generated by Django 2.2.16 on 2024-09-21 09:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_auto_20240921_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
