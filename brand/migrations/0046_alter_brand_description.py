# Generated by Django 3.2.10 on 2023-03-20 06:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0045_alter_brand_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
