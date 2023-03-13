from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.CharField(max_length=20, primary_key=True, editable=False, unique=True)
    username = models.CharField(max_length=150, unique=True, blank=False)
    email = models.EmailField(unique=True, blank=False)
    gender = models.CharField(max_length=7, blank=False)
    phone_no = models.CharField(max_length=14, blank=False)
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


class CoreTeam(models.Model):
    id = models.CharField(max_length=20, primary_key=True, editable=False, unique=True)
    member = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    role = models.CharField(max_length=50, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Core Team'
        ordering = ['member']

    def __str__(self):
        return f'{self.member}'


class TechTeam(models.Model):
    id = models.CharField(primary_key=True, max_length=20, unique=True, editable=False)
    name = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    role = models.CharField(max_length=30, blank=False)
    team = models.CharField(max_length=70, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Technical Teams'
        ordering = ['name', 'team']

    def __str__(self):
        return f'{self.name}'


class Sessions(models.Model):
    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    speaker = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    event = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    venue = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=50, blank=False)
    day = models.DateTimeField(blank=False)
    images = models.ImageField(upload_to='Event-Images/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Sessions'
        ordering = ['-created']

    def __str__(self):
        return f'{self.event}'


