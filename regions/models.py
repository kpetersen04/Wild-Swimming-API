from django.db import models

class Region(models.Model):
    region_name = models.CharField(max_length=40)
    description = models.TextField(max_length=1000, blank=True)
    #all_sites = models.
    # -> Do I actually need this? If I have regionId location on the swim_site.region? Add later if so
    # How do I only get the swim_sites that are relevant to that specific region? 

    def __str__(self):
        return f"{self.region_name}"