from django.db import models

class Restaurant(models.Model):
    image = models.ImageField(null=True,blank=True)
    name = models.CharField(max_length=120)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
