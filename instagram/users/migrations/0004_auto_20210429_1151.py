# Generated by Django 3.2 on 2021-04-29 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210429_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='follower',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='following',
        ),
    ]