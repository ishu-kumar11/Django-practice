from django.db import models

class UserLocation(models.Model):
    name = models.CharField(max_length=100)
    society_landmark = models.CharField(max_length=200, blank=True, null=True) 

    full_address = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)

    latitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)


    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
