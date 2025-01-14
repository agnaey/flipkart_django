# Generated by Django 5.1.2 on 2024-12-30 07:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_buy_is_confirmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buy',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.AddField(
            model_name='buy',
            name='category',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='app.categorys'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='category',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='app.categorys'),
            preserve_default=False,
        ),
    ]
