# Generated by Django 5.0.3 on 2024-04-21 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_rename_location_blogstories_city_blogstories_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogstories',
            name='country',
            field=models.CharField(max_length=255),
        ),
    ]
