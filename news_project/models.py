from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length = 120)
    
    def __str__(self):
        return self.name

class News(models.Model):
    class Status(models.TextChoices):
        Draft = "DT", "Draft"
        Published = "PB", "Published"

    title = models.CharField(max_length=120)
    slug = models.CharField(max_length=120)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(timezone.now)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Draft)

    class Meta:
        ordering = ("-published_at", )

    def __str__(self):
        return self.title