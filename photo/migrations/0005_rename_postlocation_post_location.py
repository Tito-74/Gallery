# Generated by Django 3.2.8 on 2021-10-12 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_rename_location_post_postlocation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='postLocation',
            new_name='location',
        ),
    ]
