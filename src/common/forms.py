"""Common forms."""

from django.forms import DateInput, ModelForm, Textarea, TextInput, TimeInput

from .models import News


class NewsForm(ModelForm):
    """News entity edit form."""

    class Meta:
        """Form parameters definition."""

        model = News
        fields = ("title", "annotation", "text", "author", "published_at")

        widgets = {
            "title": TextInput(
                attrs={"class": "form-control", "placeholder": "News title"}
            ),
            "annotation": TextInput(
                attrs={"class": "form-control", "placeholder": "Annotation"}
            ),
            "text": Textarea(
                attrs={"class": "form-control", "placeholder": "News text"}
            ),
            "published_at": DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                    "placeholder": "Published at",
                }
            ),
            "author": TextInput(
                attrs={"class": "form-control", "placeholder": "Author"}
            ),
        }
