# Generated by Django 4.1.7 on 2023-04-24 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1_api', '0025_remove_company_ind_company_name_auto_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='person',
            name='ind_person_name_auto',
        ),
        migrations.AddIndex(
            model_name='company',
            index=models.Index(fields=['reputation', 'id'], name='ind_company_reputation'),
        ),
    ]