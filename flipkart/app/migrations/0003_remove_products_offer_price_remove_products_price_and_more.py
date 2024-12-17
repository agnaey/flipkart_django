# Generated by Django 5.1.2 on 2024-12-16 07:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_products_laptop_products_others_buy_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='offer_price',
        ),
        migrations.RemoveField(
            model_name='products',
            name='price',
        ),
        migrations.CreateModel(
            name='Categorys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storage', models.TextField()),
                ('color', models.TextField()),
                ('price', models.TextField()),
                ('offer_price', models.TextField()),
                ('size', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.products')),
            ],
        ),
    ]