# Generated by Django 3.2.8 on 2021-10-11 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='location',
            new_name='postLocation',
        ),
    ]
