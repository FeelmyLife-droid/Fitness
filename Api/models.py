from django.db import models


class Club(models.Model):
    password = models.TextField()
    username = models.TextField()
    club_id = models.TextField()
    api_url = models.TextField()

# Create your models here.
