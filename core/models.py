from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class About(models.Model):
    profile_picture = models.ImageField(default="core/default.png")
    name = models.CharField(max_length=25)
    role = models.CharField(max_length=30)


class Experience(models.Model):
    position = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    company_location = models.CharField(max_length=50)
    about = models.TextField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)


class Education(models.Model):
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    institution = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()


class Professional(models.Model):
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField(default="core/default.png", upload_to='core/media/core')
    about = models.TextField()
    date = models.DateTimeField(default=timezone.now)
