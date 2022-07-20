# Generated by Django 4.0.4 on 2022-07-17 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CR_Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('T_Full_Name', models.CharField(max_length=100)),
                ('T_Email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('T_Sup_Series', models.IntegerField(default=0)),
                ('T_Sup_Section', models.CharField(default='x', max_length=1)),
                ('T_Department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CR_Home.department')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('S_Roll', models.IntegerField(primary_key=True, serialize=False)),
                ('S_Full_Name', models.CharField(max_length=100)),
                ('S_Series', models.IntegerField()),
                ('S_Section', models.CharField(max_length=1)),
                ('S_Reg_No', models.IntegerField()),
                ('S_Prev_Earned_C', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('S_Department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CR_Home.department')),
                ('S_Semester', models.ForeignKey(default='NA', on_delete=django.db.models.deletion.PROTECT, to='CR_Home.semester')),
                ('S_Year', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='CR_Home.year')),
            ],
        ),
        migrations.AddConstraint(
            model_name='student',
            constraint=models.UniqueConstraint(fields=('S_Roll', 'S_Reg_No'), name='unique_Roll_Reg'),
        ),
    ]
