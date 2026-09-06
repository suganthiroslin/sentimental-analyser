from django.db import models
from django.contrib.auth.models import User


class SentimentHistory(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    text = models.TextField()

    platform = models.CharField(
        max_length=100,
        blank=True
    )

    sentiment = models.CharField(
        max_length=20
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return f"{self.user.username} - {self.sentiment}"