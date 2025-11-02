from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=50)
    body=models.CharField(max_length=1000)
    created_at=models.DateTimeField(default=timezone.now)
    modified_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title