# Generated by Django 4.2.5 on 2023-09-26 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
