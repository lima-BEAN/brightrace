from django.contrib import admin

# Register your models here.
from shop.models import Category, Product, Coupon

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Coupon)
