# Generated by Django 4.2 on 2023-05-02 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_auth', '0004_remove_user_favorite_sites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.URLField(blank=True),
        ),
    ]