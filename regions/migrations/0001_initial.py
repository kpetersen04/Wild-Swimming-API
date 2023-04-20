# Generated by Django 4.2 on 2023-04-20 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True, max_length=400)),
            ],
        ),
    ]
