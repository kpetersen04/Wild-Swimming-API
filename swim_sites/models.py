from django.db import models

class Swim_site(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey('regions.Region', related_name='swim_sites', on_delete=models.CASCADE)
    location = models.CharField(max_length=7) # should be a postcode
    description = models.TextField(max_length=400, blank=True)
    image = models.URLField(blank=True)
    parking_info = models.CharField(max_length=100, blank=True)
    # site_comments = models.ForeignKey('comments.Comment', related_name='swim_sites', on_delete=models.CASCADE, blank=True, null=True)
    # rating = 

    def __str__(self):
        return f"{self.name} - {self.region}"
