# Generated by Django 3.1.4 on 2021-01-06 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20210106_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
