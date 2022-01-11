# Generated by Django 4.0.1 on 2022-01-10 11:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_openjobs_jobname_openjobs_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliedjobs',
            name='apply_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='openjobs',
            name='close_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='openjobs',
            name='open_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
