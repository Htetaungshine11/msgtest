from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Cuser(AbstractUser):
    email = models.EmailField(verbose_name='email address', unique=True)
    USERNAME_FIELD="email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS=["username",]
