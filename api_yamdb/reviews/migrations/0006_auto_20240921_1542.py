# Generated by Django 2.2.16 on 2024-09-21 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20240921_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='confirmation_code',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
