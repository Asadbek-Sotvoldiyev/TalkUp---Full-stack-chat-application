from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

STATUS_CHOICES = (
    ('online', 'online'),
    ('offline', 'offline'),
)


class User(AbstractUser):
    photo_url = models.ImageField(upload_to='user_avatars/', blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    bio = models.CharField(max_length=100, null=True, blank=True)
    is_online = models.BooleanField(default=False)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='offline')

    def __str__(self):
        return f"{self.username} | {self.first_name} {self.last_name}"

