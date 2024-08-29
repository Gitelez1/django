from django.db import models
from django.utils import timezone

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255, default="Unknown")
    release_date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)  # Temporarily use default
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
