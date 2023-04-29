from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField()
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True)
    bio = models.TextField(max_length=400, blank=True)
    # locations_rated = models.ManyToManyField('swim_sites.Swim_site', blank=True)
    # followers = 
    # following = 

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'



