# Generated by Django 4.1.7 on 2023-04-24 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1_api', '0022_company_avg_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='avg_salary',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=12, null=True),
        ),
    ]