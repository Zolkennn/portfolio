from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.CharField(max_length=24)
    lien = models.CharField(max_length=256)