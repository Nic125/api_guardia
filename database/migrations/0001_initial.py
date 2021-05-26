# Generated by Django 3.1.6 on 2021-05-26 01:23

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Guard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('duration_hs', models.CharField(max_length=11)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Guardia',
                'verbose_name_plural': 'Guardias',
            },
        ),
        migrations.CreateModel(
            name='NotWorkingDays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=70)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.department')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.CharField(max_length=30, unique=True)),
                ('d', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('profession', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('is_pro', models.CharField(max_length=10)),
                ('is_active', models.CharField(default='yes', max_length=10)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.service')),
            ],
            options={
                'verbose_name': 'Personal',
                'verbose_name_plural': 'Personal',
            },
        ),
        migrations.CreateModel(
            name='GuardSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('is_working_day', models.CharField(max_length=25)),
                ('is_active', models.CharField(default='no', max_length=10)),
                ('shift', models.CharField(default='24', max_length=20)),
                ('is_extra', models.CharField(default='no', max_length=10)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('guard_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.guard')),
                ('personal_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.personal')),
            ],
            options={
                'verbose_name': 'Planilla guardia',
                'verbose_name_plural': 'Planillas guardias',
            },
        ),
        migrations.AddField(
            model_name='guard',
            name='service_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.service'),
        ),
    ]