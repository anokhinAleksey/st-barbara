"""Module for the translation extension clases of models."""

from modeltranslation.translator import TranslationOptions, register

from .models import News, Page


@register(News)
class NewsTranslationOptions(TranslationOptions):
    """Translation extension model for News model."""

    fields = ("title", "annotation", "text")


@register(Page)
class PageTranslationOptions(TranslationOptions):
    """Translation extension model for Page model."""

    fields = ("text",)
