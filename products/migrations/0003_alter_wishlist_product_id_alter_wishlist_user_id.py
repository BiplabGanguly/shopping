# Generated by Django 4.1.4 on 2023-02-26 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='product_id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='user_id',
            field=models.CharField(max_length=255),
        ),
    ]