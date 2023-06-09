# Generated by Django 4.1.7 on 2023-04-24 13:43

import django.core.validators
from django.db import migrations, models
import django.db.models.functions.text


class Migration(migrations.Migration):

    dependencies = [
        ('a1_api', '0023_alter_company_avg_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=75, unique=True, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterUniqueTogether(
            name='personworkingatcompany',
            unique_together={('person', 'company')},
        ),
        migrations.AddIndex(
            model_name='company',
            index=models.Index(fields=['name'], include=('id',), name='ind_company_name_auto'),
        ),
        migrations.AddIndex(
            model_name='company',
            index=models.Index(fields=['avg_salary', 'id'], name='ind_comp_avg_salary'),
        ),
        migrations.AddIndex(
            model_name='personworkingatcompany',
            index=models.Index(fields=['company'], include=('salary',), name='ind_company'),
        ),
    ]
