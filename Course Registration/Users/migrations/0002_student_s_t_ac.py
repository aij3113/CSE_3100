# Generated by Django 4.0.4 on 2022-08-16 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='S_T_AC',
            field=models.BooleanField(default=False),
        ),
    ]
