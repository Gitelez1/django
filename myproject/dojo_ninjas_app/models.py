# dojo_ninjas_app/models.py
from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(default='old dojo')  # Add this line for the final step

    def __str__(self):
        return self.name

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name='ninjas', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
