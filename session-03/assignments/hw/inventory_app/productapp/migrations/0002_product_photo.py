# Generated by Django 3.2.3 on 2021-05-22 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(default=0, height_field=150, upload_to='products', width_field=150),
            preserve_default=False,
        ),
    ]
