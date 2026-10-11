from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Contact, Post


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject")
    readonly_fields = ("created_at",)


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ("title", "slug", "is_published", "published_at")
    list_filter = ("is_published",)
    search_fields = ("title", "content")
    prepopulated_fields = {}
