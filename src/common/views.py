"""Common app views."""

import os

from django.shortcuts import render
from django.views.generic import DetailView, UpdateView

from .forms import NewsForm
from .models import News, Page


def home(request):
    """View for main page."""
    news = News.objects.order_by("-created_at")[:10]

    return render(request, "common/home.html", {"news": news})


class NewsDetailView(DetailView):
    """News detail view page."""

    model = News
    template_name = "common/news-detail-view.html"
    context_object_name = "news"


class NewsEditView(UpdateView):
    """News edit view page."""

    model = News
    template_name = "common/edit-news.html"

    form_class = NewsForm


def about(request):
    """View for about page."""
    return render(request, "common/about.html")


def contacts(request):
    """View for contacts page."""
    return render(request, "common/contacts.html")


def editor(request):
    """View for list of static pages."""
    pages = Page.objects.order_by("-date")[:10]

    return render(request, "common/editor.html", {"pages": pages})
