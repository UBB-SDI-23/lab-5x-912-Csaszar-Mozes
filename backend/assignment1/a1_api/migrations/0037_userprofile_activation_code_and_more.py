# Generated by Django 4.1.7 on 2023-05-05 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1_api', '0036_alter_company_avg_salary_alter_company_net_value_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='activation_code',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='code_requested_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]