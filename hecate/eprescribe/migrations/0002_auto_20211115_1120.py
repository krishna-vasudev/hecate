# Generated by Django 3.2.3 on 2021-11-15 05:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eprescribe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='prescription',
            name='disease_description',
            field=models.CharField(default='N/A', max_length=300),
        ),
    ]