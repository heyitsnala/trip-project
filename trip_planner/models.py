from django.db import models

# Create your models here.


class Trip(models.Model):
    user = models.CharField(max_length=20)
    location = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    startDate = models.DateField(null=True, blank=True)
    endDate = models.DateField(null=True, blank=True)
    packing = models.TextField(null=True, blank=True)
    places = models.TextField(null=True, blank=True)
    activities = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.location

