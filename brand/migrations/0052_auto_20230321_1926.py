# Generated by Django 3.2.10 on 2023-03-21 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0051_brand_terms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
