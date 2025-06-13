from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password

from apps.system.models import BaseModel
from apps.users.constants import COUNTRY_CHOICES, ROLE_CHOICES

class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    """
    User model that extends AbstractBaseUser and PermissionsMixin.
    """
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES, default='India')
    languages_known = models.JSONField(default=list)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='USER')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']      

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
