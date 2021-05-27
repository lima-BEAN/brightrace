from django.db import models

# Create your models here.
class Product(models.Model):

    AUTO        = 'Auto'
    BEAUTY      = 'Beauty'
    GROCERIES   = 'Groceries'
    OUTDOORS    = 'Outdoors'
    TECH        = 'Tech'

    CATEGORY_CHOICES = [
        (AUTO, 'Auto'),
        (BEAUTY, 'Beauty'),
        (GROCERIES, 'Groceries'),
        (OUTDOORS, 'Outdoors'),
        (TECH, 'Tech'),
    ]

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price =  models.FloatField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default=TECH)
    photo = models.ImageField(upload_to='products')

    def __str__(self):
        return self.name
