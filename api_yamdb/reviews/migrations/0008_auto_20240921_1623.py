# Generated by Django 2.2.16 on 2024-09-21 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_comment_genre_review_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='review_id',
            new_name='review',
        ),
    ]
