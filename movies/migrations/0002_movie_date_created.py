# Generated by Django 4.1.7 on 2023-03-13 21:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 13, 21, 7, 0, 26012, tzinfo=datetime.timezone.utc)),
        ),
    ]
