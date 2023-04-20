from django.db import models

class Comment(models.Model):
    text = models.CharField(max_length=300)
    site = models.ForeignKey('swim_sites.Swim_site', related_name='comments', on_delete=models.CASCADE)
    created_by =  models.ForeignKey('jwt_auth.User', related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.text} - {self.created_by}"