# Generated by Django 4.1 on 2024-05-01 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_accommodation_slug_decoration_slug_destination_slug_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('service', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
            options={
                'db_table': 'contact',
            },
        ),
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
