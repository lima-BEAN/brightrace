# Generated by Django 3.2.3 on 2021-05-27 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0014_auto_20210527_0619'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
