from django.db import models
from django.conf import settings

from datetime import datetime

class Tags(models.Model):
    name = models.CharField(max_length=11)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(null=False, blank=False, max_length=200)
    text = models.TextField(null=True, blank=True)
    tags = models.ForeignKey(Tags, null=True, blank=True)
    active = models.BooleanField(default=True)  # If post is visible or not
    publish = models.DateTimeField(default=datetime.now)  # When to publish post
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
