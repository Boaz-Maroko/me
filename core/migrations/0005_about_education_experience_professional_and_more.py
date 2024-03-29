# Generated by Django 5.0.3 on 2024-03-11 20:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_homepage_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(default='core/default.png', upload_to='core/media/core')),
                ('name', models.CharField(max_length=25)),
                ('role', models.CharField(max_length=30)),
                ('welcome', models.CharField(max_length=50)),
                ('introduction', models.TextField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('institution', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('position', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=50)),
                ('company_location', models.CharField(max_length=50)),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('thumbnail', models.ImageField(default='core/default.png', upload_to='core/media/core')),
                ('about', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='Homepage',
        ),
        migrations.DeleteModel(
            name='Works',
        ),
    ]
