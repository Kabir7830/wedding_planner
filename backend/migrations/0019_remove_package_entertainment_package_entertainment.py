# Generated by Django 4.1 on 2024-05-09 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0018_remove_package_entertainment_package_entertainment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='entertainment',
        ),
        migrations.AddField(
            model_name='package',
            name='entertainment',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
