# Generated by Django 4.1.7 on 2023-03-11 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a1_api', '0004_alter_location_apartment_alter_location_county'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='hq_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='a1_api.location'),
        ),
        migrations.AlterField(
            model_name='location',
            name='apartment',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='county',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
