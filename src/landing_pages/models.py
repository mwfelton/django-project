from django.db import models

class LandingPageEntry(models.Model):
    name = models.CharField(max_length=220)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

def __str__(self):
    return f"{self.email}"