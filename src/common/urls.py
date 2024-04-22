"""Common app urls config."""

from common import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("news/<int:pk>", views.NewsDetailView.as_view(), name="news-detail"),
    path("about", views.about, name="about"),
    path("contacts", views.contacts, name="contacts"),
    path("editor", views.editor, name="editor"),
]
