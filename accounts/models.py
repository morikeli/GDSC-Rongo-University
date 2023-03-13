from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.CharField(max_length=20, primary_key=True, editable=False, unique=True)
    username = models.CharField(max_length=150, unique=True, blank=False)
    email = models.EmailField(unique=True, blank=False)
    gender = models.CharField(max_length=7, blank=False)
    phone_no = models.CharField(max_length=14, blank=False)
    bio = models.TextField(blank=False)
    profile_pic = models.ImageField(upload_to='Users-Dps/', default='default.png')
    school = models.CharField(max_length=70, blank=False)
    year = models.CharField(max_length=20, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name_plural = 'Members'
        ordering = ['username']

    def __str__(self):
        return f'{self.username}'

