# Generated by Django 4.1.7 on 2023-03-19 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0040_alter_brand_description_alter_brand_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='description',
            field=models.TextField(),
        ),
    ]