# Generated by Django 3.2.10 on 2023-03-22 08:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0059_alter_brand_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
