# Generated by Django 4.0.4 on 2022-07-25 08:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='S_C_End_D',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='student',
            name='S_C_Start_D',
            field=models.DateField(default='2099-01-01'),
        ),
    ]