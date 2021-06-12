# Generated by Django 3.2.3 on 2021-05-23 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0005_alter_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Auto', 'Auto'), ('Beauty', 'Beauty'), ('Groceries', 'Groceries'), ('Outdoors', 'Outdoors'), ('Tech', 'Tech')], default='Tech', max_length=10),
        ),
    ]