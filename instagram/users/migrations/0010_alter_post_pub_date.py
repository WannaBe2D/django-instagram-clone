# Generated by Django 3.2 on 2021-05-05 13:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210505_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 5, 13, 16, 53, 926506, tzinfo=utc)),
        ),
    ]
