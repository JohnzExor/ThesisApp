from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager


# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    the_one_who_posted = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="capstone_posts"
    )
    abstract = models.TextField()

    authors = models.CharField(max_length=500)
    adviser = models.CharField(max_length=250)
    panels = models.CharField(max_length=500)

    status = models.CharField(
        max_length=3, choices=Status.choices, default=Status.DRAFT
    )

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    tags = TaggableManager()

    class Meta:
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"]),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "thesis:thesis_details",
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
        )
class Comment(models.Model):
    post = models.ForeignKey(Post, 
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email=models.EmailField()
    body= models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering=['created']
        indexes = [
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'

