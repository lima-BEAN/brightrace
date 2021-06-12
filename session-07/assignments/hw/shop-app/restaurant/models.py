from django.db import models

# Create your models here.
# from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    street = models.CharField(max_length=50, blank=True, null=True)
    number = models.PositiveIntegerField(blank=True, null=True)
    city = models.CharField(max_length=30)
    zipCode = models.CharField(max_length=5, blank=True, null=True)
    stateOrProvince = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=25, blank=True, null=True)
    telephone = models.IntegerField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('restaurant:restaurant_detail', kwargs={'pk': self.pk})


class Dish(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField('$ amount', max_digits=8, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    image = models.ImageField(upload_to="restaurant/", blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, null=True, related_name='dishes', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'dish'
        verbose_name_plural = 'dishes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('restaurant:dish_detail', kwargs={'pkr': self.restaurant.pk, 'pk': self.pk}) #reverse mapping


RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))


class Review(models.Model):
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True


class RestaurantReview(Review):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
