# Generated by Django 3.2.10 on 2023-03-21 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0053_auto_20230321_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='logo',
            field=models.URLField(blank=True, null=True),
        ),
    ]
