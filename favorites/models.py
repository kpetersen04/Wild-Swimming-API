from django.db import models

class Favorite(models.Model):
    site = models.ForeignKey('swim_sites.Swim_site', related_name='favorites', on_delete=models.CASCADE)
    created_by =  models.ForeignKey('jwt_auth.User', related_name='favorites', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.site} - {self.created_by}"
