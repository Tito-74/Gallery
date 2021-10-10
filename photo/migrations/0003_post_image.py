# Generated by Django 3.2.8 on 2021-10-09 15:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_post_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='posts/'),
            preserve_default=False,
        ),
    ]