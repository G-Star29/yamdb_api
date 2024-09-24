# Generated by Django 2.2.16 on 2024-09-21 09:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_auto_20240921_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
