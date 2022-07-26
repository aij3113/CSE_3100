# Generated by Django 4.0.4 on 2022-08-16 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('D_Name', models.CharField(max_length=7, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Reg_St_Sem',
            fields=[
                ('rs', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('semester', models.CharField(max_length=6, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('year', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Stu_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SC_Roll', models.IntegerField()),
                ('SC_Code', models.CharField(max_length=15)),
                ('SC_Series', models.IntegerField()),
                ('SC_Section', models.CharField(default='X', max_length=1)),
                ('SC_T_AC', models.BooleanField(default=False)),
                ('SC_Dept', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CR_Home.department')),
                ('SC_RS_Sem', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CR_Home.reg_st_sem')),
                ('SC_Semester', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CR_Home.semester')),
                ('SC_Year', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CR_Home.year')),
            ],
        ),
        migrations.CreateModel(
            name='Stu_CBR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SCBR_Roll', models.IntegerField()),
                ('SCBR_Series', models.IntegerField()),
                ('SCBR_Section', models.CharField(default='X', max_length=1)),
                ('SCBR_Slip', models.FileField(upload_to='Slips/')),
                ('SCBR_Dept', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CR_Home.department')),
                ('SCBR_RS_Sem', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CR_Home.reg_st_sem')),
                ('SCBR_Sem', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CR_Home.semester')),
                ('SCBR_Year', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CR_Home.year')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_Code', models.CharField(max_length=10)),
                ('C_Title', models.CharField(max_length=100)),
                ('C_Credit', models.DecimalField(decimal_places=2, max_digits=5)),
                ('C_Department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CR_Home.department')),
                ('C_Semester', models.ForeignKey(default='NA', on_delete=django.db.models.deletion.PROTECT, to='CR_Home.semester')),
                ('C_Year', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='CR_Home.year')),
            ],
        ),
        migrations.AddConstraint(
            model_name='stu_course',
            constraint=models.UniqueConstraint(fields=('SC_Roll', 'SC_Code', 'SC_RS_Sem', 'SC_Series'), name='unique_sc'),
        ),
        migrations.AddConstraint(
            model_name='stu_cbr',
            constraint=models.UniqueConstraint(fields=('SCBR_Roll', 'SCBR_Year', 'SCBR_Sem', 'SCBR_Series'), name='unique_scbr'),
        ),
        migrations.AddConstraint(
            model_name='course',
            constraint=models.UniqueConstraint(fields=('C_Code', 'C_Department'), name='unique_course'),
        ),
    ]
