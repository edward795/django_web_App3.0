# Generated by Django 4.0 on 2022-01-02 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterCandidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('state', models.TextField()),
                ('pincode', models.IntegerField()),
                ('phoneno', models.IntegerField()),
                ('qualification', models.TextField()),
                ('jobtype', models.TextField()),
                ('skills', models.TextField()),
                ('experience', models.TextField()),
                ('comments', models.TextField()),
            ],
        ),
    ]