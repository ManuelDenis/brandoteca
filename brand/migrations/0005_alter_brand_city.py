# Generated by Django 4.1.7 on 2023-03-13 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0004_alter_brand_main_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='city',
            field=models.CharField(choices=[('Alba, Abrud', 'Alba, Abrud'), ('Alba, Abrud-Sat', 'Alba, Abrud-Sat'), ('Alba, Achimetesti', 'Alba, Achimetesti'), ('Alba, Acmariu', 'Alba, Acmariu'), ('Alba, Aiud', 'Alba, Aiud')], max_length=50),
        ),
    ]
