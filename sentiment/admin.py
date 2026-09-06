from django.contrib import admin

from .models import SentimentHistory


@admin.register(SentimentHistory)
class SentimentHistoryAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'platform',
        'sentiment',
        'created_at'
    )

    list_filter = (
        'sentiment',
        'platform',
        'created_at'
    )

    search_fields = (
        'user__username',
        'text',
    )