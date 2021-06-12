from django.db import models

# Create your models here.
class Employee(models.Model):

    DEPARTMENT_CHOICES = (('01', '01'),('02', '02'), ('03', '03'))

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    salary = models.FloatField()
    department = models.CharField(
        max_length=2,
        choices=DEPARTMENT_CHOICES,
        default='01'
    )


    def __str__(self):
        return self.first_name
