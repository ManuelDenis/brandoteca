# Generated by Django 4.1.7 on 2023-03-17 09:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0022_alter_brand_created_at_alter_brand_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 17, 11, 7, 45, 136761)),
        ),
        migrations.AlterField(
            model_name='brand',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 17, 11, 7, 45, 136761)),
        ),
    ]
