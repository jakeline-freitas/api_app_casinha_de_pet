from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.expressions import F

class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    phone = models.CharField(max_length=55)
    first_name = None
    last_name = None


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

