# Generated by Django 4.2 on 2023-04-29 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swim_sites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swim_site',
            name='postcode',
            field=models.CharField(max_length=8),
        ),
    ]