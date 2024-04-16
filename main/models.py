from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    lien = models.CharField(max_length=256)


class Tags(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tags = models.CharField(max_length=24, null=True)
