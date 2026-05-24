"""
Model translation registration.
Defines which fields should be translated for bilingual support.
"""

from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Tag, Post, Project


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


class TagTranslationOptions(TranslationOptions):
    fields = ('name',)


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'excerpt', 'content', 'meta_description', 'meta_keywords')


class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


# Register translations
translator.register(Category, CategoryTranslationOptions)
translator.register(Tag, TagTranslationOptions)
translator.register(Post, PostTranslationOptions)
translator.register(Project, ProjectTranslationOptions)