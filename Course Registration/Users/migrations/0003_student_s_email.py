# Generated by Django 4.0.4 on 2022-09-10 17:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_student_s_t_ac'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='S_Email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
    ]
