# Generated by Django 3.2.3 on 2021-05-27 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0011_remove_product_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, upload_to='products/'),
        ),
    ]