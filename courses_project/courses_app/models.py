from django.db import models
from django.core.exceptions import ValidationError

class Description(models.Model):
    content = models.TextField()

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.OneToOneField(Description, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if len(self.name) <= 5:
            raise ValidationError('Course name must be more than 5 characters')
        if len(self.description.content) <= 15:
            raise ValidationError('Description must be more than 15 characters')
        super().save(*args, **kwargs)

class Comment(models.Model):
    course = models.ForeignKey(Course, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

