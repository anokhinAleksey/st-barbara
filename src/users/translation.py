"""Module for the translation extension clases of models."""

from modeltranslation.translator import TranslationOptions, register

from .models import User


@register(User)
class UserTranslationOptions(TranslationOptions):
    """Translation extension model for User."""

    fields = ("first_name", "last_name")
