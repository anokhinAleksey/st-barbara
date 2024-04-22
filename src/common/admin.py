"""Admin interfaces."""

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import News, Page


class NewsAdmin(TranslationAdmin):
    """Admin interface for News model."""

    list_display = ("title", "author", "published_at", "created_at")


class PageAdmin(TranslationAdmin):
    """Admin interface for News model."""

    list_display = ("text",)


admin.site.register(News, NewsAdmin)
admin.site.register(Page, PageAdmin)
