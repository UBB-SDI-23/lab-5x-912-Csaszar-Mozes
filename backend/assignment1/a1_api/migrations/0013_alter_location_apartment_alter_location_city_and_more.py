# Generated by Django 4.1.7 on 2023-04-08 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1_api', '0012_remove_location_county_alter_location_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='apartment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='street',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='personworkingatcompany',
            name='role',
            field=models.CharField(max_length=125),
        ),
    ]
