from django.db import models
# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User


class UserProfile(models.Model):
    firstName = models.CharField(max_length=50, blank=True)
    lastName = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    phoneNumber = models.TextField(max_length=50, blank=True)
    birthday = models.DateField()
    SUBJECT_CHOICES = (
        ('Subject 1', 'Subject 1'),
        ('Subject 2', 'Subject 2'),
        ('Subject 3', 'Subject 3'),
    )
    subject = models.CharField(max_length=20, blank=True, choices=SUBJECT_CHOICES)
    is_male = models.BooleanField("IS Male", default=False,)
    is_female = models.BooleanField("IS Female", default=False)

    def __str__(self):
        return self.firstName
