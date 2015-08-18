from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.
# this model replaces default django user model


class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    # password field defiend in base class
    last_4_digits = models.CharField(max_length=4, blank=True, null=True)
    strip_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
