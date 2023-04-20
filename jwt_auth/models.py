from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField()
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    # profile_photo = models.ImageField(upload_to='profile_photos')
    profile_photo = models.CharField(max_length=300)
    # add a subdirectory called 'profile_photos' within the media directory of your project
    bio = models.TextField(max_length=400)
    favorite_sites = models.ManyToManyField('swim_sites.Swim_site', blank=True)
    all_comments = models.ForeignKey('comments.Comment', related_name='users', on_delete=models.CASCADE, blank=True, null=True)
    # locations_rated = models.ManyToManyField('swim_sites.Swim_site', blank=True)
    # followers = 
    # following = 

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'



