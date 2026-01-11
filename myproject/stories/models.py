from django.db import models

# Create your models here.
from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=255)

class Chapter(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="chapters")
    index = models.IntegerField()
    title = models.CharField(max_length=255)
    content = models.TextField()
