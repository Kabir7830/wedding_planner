# Generated by Django 4.1 on 2024-05-03 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_services_is_published_services_provider_company_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
