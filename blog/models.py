from django.db import models
from django.urls import reverse
from django.utils import timezone


class Contact(models.Model):
    """Represents a contact form submission."""

    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    """A bilingual (EN/FA) article. Translated fields get _en / _fa columns."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True,
                            help_text="Used in the URL. Persian slugs are allowed.")
    excerpt = models.CharField(max_length=300, blank=True,
                               help_text="Short summary shown in lists and used as meta description.")
    content = models.TextField(help_text="Markdown supported.")
    cover_image = models.ImageField(upload_to="posts/", blank=True, null=True)
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})
