from django.db import models

class LandingPageEntry(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
