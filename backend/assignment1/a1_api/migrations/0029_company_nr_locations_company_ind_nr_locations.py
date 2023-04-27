# Generated by Django 4.1.7 on 2023-04-26 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1_api', '0028_alter_personworkingatcompany_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='nr_locations',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddIndex(
            model_name='company',
            index=models.Index(fields=['nr_locations', 'id'], name='ind_nr_locations'),
        ),
    ]