# Generated by Django 3.0.1 on 2019-12-22 13:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191222_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 22, 13, 40, 11, 487417, tzinfo=utc)),
        ),
    ]