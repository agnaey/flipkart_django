# Generated by Django 5.1.2 on 2024-12-25 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_products_offer_price_remove_products_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
