from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class StreamPlatform(models.Model):
    """Define Movie Streaming platform model"""
    name = models.CharField(max_length=80)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=200)

    def __str__(self) -> str:
        return self.name


class WatchList(models.Model):
    """Define Movie database"""

    title = models.CharField(max_length=100)
    platform = models.ForeignKey(
        StreamPlatform, on_delete=models.CASCADE, related_name='watchlist')
    storyline = models.CharField(max_length=200)
    total_reviews = models.IntegerField(default=0)
    avg_rating = models.FloatField(default=0)
    active = models.BooleanField(default=True)
    crated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    """Define Movie review data model"""

    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveBigIntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1), ])
    message = models.CharField(max_length=200)
    watchlist = models.ForeignKey(
        WatchList, on_delete=models.CASCADE, related_name="reviews")
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"({self.rating}): {self.watchlist.title} by {self.review_user.username}"
