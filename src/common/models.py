"""Common app models."""

from django.db import models


class News(models.Model):
    """News model."""

    title = models.CharField(max_length=255)
    annotation = models.CharField(max_length=255, blank=True)
    text = models.TextField()
    author = models.CharField(max_length=255)
    published_at = models.DateTimeField("date published")
    created_at = models.DateTimeField("date created")

    def __str__(self) -> str:
        """Model sring representation."""
        return self.title


class Page(models.Model):
    """Page model."""

    name = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField("date created")

    def __str__(self) -> str:
        """Model sring representation."""
        return self.name
