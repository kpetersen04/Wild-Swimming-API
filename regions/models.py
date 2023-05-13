from django.db import models

class Region(models.Model):
    region_name = models.CharField(max_length=40)
    description = models.TextField(max_length=1000, blank=True)
    def __str__(self):
        return f"{self.region_name}"