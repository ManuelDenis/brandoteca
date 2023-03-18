# Generated by Django 4.1.7 on 2023-03-16 08:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0018_alter_brand_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='brand',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='brand',
            name='is_brand_of_the_month',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='brand',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='brand',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]