# Generated by Django 4.1.7 on 2023-03-11 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a1_api', '0002_alter_person_age_alter_person_income'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('county', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('apartment', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
                ('net_value', models.IntegerField()),
                ('reputation', models.IntegerField()),
                ('hq_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='a1_api.location')),
            ],
        ),
    ]
