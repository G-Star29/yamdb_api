# Generated by Django 2.2.16 on 2024-09-21 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20240920_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='confirmation_code',
            field=models.IntegerField(default=None),
        ),
    ]
