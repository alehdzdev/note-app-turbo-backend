# Django
from django.conf import settings
from django.db import models


class Note(models.Model):
    """A note belonging to a single user."""

    class Category(models.TextChoices):
        RANDOM_THOUGHTS = "Random Thoughts"
        SCHOOL = "School"
        PERSONAL = "Personal"

    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    color = models.CharField(max_length=7, default="#ffffff")
    category = models.CharField(max_length=50, choices=Category.choices)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notes",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
