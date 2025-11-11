from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "rating", "published_at")
    list_filter = ("status", "rating", "created_at", "published_at")
    search_fields = ("title", "body", "author__username")
    ordering = ("-published_at",)
