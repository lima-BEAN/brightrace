from django.db import models

# Create your models here.
class Product(models.Model):

    AUTO        = 'AU'
    BEAUTY      = 'BE'
    GARDEN      = 'GA'
    GROCERY     = 'GR'
    OUTDOORS    = 'OU'
    PETS        = 'PE'
    TECH        = 'TE'

    CATEGORY_CHOICES = [
        (AUTO, 'Auto'),
        (BEAUTY, 'Beauty'),
        (GARDEN, 'Garden'),
        (GROCERY, 'Grocery'),
        (OUTDOORS, 'Outdoors'),
        (PETS, 'Pet'),
        (TECH, 'Tech'),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=TECH)
    description = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.name
