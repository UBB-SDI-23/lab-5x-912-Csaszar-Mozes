# Generated by Django 4.1.7 on 2023-04-24 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a1_api', '0018_remove_person_ind_person_name_auto_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='personworkingatcompany',
            name='ind_company',
        ),
    ]
