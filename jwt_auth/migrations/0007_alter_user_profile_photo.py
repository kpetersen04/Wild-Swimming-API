# Generated by Django 4.2 on 2023-05-04 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_auth', '0006_alter_user_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.URLField(blank=True, default='https://res.cloudinary.com/de7f0or8o/image/upload/v1683182954/rvgeonbagoc3ym6jodkt.webp'),
        ),
    ]
