# Generated by Django 3.2.3 on 2021-05-27 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0027_product_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='customer',
        ),
    ]
