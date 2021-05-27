# Generated by Django 3.2.3 on 2021-05-27 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0020_auto_20210527_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('Auto', 'Auto'), ('Beauty', 'Beauty'), ('Groceries', 'Groceries'), ('Outdoors', 'Outdoors'), ('Tech', 'Tech')], default='Tech', max_length=10),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
