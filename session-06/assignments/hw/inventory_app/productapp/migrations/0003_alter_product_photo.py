# Generated by Django 3.2.3 on 2021-05-22 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0002_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(upload_to='products'),
        ),
    ]
