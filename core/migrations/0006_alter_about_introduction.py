# Generated by Django 5.0.3 on 2024-03-11 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_about_education_experience_professional_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='introduction',
            field=models.TextField(max_length=1000),
        ),
    ]