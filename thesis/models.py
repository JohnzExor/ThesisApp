from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        APPROVED = "APP", "Approved"
        PENDING = "PEN", "Pending"
        REJECTED = "REJ", "Rejected"

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    the_one_who_posted = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="capstone_posts"
    )
    abstract = models.TextField()

    authors = models.CharField(max_length=500)
    adviser = models.CharField(max_length=250)
    panels = models.CharField(max_length=500)

    status = models.CharField(
        max_length=3, choices=Status.choices, default=Status.PENDING
    )

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"]),
        ]

    def __str__(self):
        return self.title
