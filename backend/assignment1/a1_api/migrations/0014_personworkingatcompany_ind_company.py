# Generated by Django 4.1.7 on 2023-04-08 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1_api', '0013_alter_location_apartment_alter_location_city_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='personworkingatcompany',
            index=models.Index(fields=['company'], name='ind_company'),
        ),
    ]
