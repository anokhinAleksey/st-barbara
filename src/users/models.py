"""User app models."""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Model for extending and substituting built-in User model."""
