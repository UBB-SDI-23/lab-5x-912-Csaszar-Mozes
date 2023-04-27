# Generated by Django 4.1.7 on 2023-04-25 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1_api', '0027_remove_company_ind_comp_avg_salary_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='personworkingatcompany',
            unique_together={('person', 'company')},
        ),
        migrations.AddIndex(
            model_name='company',
            index=models.Index(fields=['name', 'id'], name='ind_company_name_auto'),
        ),
        migrations.AddIndex(
            model_name='company',
            index=models.Index(fields=['avg_salary', 'id'], name='ind_comp_avg_salary'),
        ),
        migrations.AddIndex(
            model_name='company',
            index=models.Index(fields=['reputation', 'id'], name='ind_company_reputation'),
        ),
        migrations.AddIndex(
            model_name='personworkingatcompany',
            index=models.Index(fields=['company'], include=('salary',), name='ind_company'),
        ),
    ]