from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User

# Create your models here.
class Customer(User):
    github = models.URLField(blank=True)

    def __str__(self):
        return self.email
