from django.db import models


# class Category(models.Model):
#     name = models.CharField(max_length=200, help_text='Enter a category (e.g. Outdoors)')
# #     slug = models.SlugField(max_length=200, db_index=True, unique=True)
# #
#     class Meta:
# #         # ordering = ('name',)
#         verbose_name = 'category'
# #         verbose_name_plural = 'categories'
# #
#     def __str__(self):
#         return self.name

    # def get_absolute_url(self):
    #     return reverse('productapp:product_list_by_category', args=[self.slug])


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
    # category = models.ForeignKey(Category, help_text='Select a genre for this book', on_delete=models.CASCADE)

    photo = models.ImageField(upload_to='products', blank=True) # TODO: fix photo not being able to load in form

    def __str__(self):
        return self.name
