from django.db import models

class TrackingNumber(models.Model):
    tracking_number = models.CharField(max_length=16, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    