# Generated by Django 3.2.3 on 2021-05-27 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0012_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, upload_to='products'),
        ),
    ]
