"""Users app urls config."""

from django.urls import path
from users.views import UserProfileView

urlpatterns = [
    path("profile", UserProfileView.as_view(), name="user-profile"),
]
