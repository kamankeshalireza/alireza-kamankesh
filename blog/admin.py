# """
# Customized Django Admin for bilingual content management.
# """

# from django.contrib import admin
# from modeltranslation.admin import TranslationAdmin
# from .models import Category, Tag, Post, Project


# @admin.register(Category)
# class CategoryAdmin(TranslationAdmin):
#     list_display = ['name', 'slug', 'created_at']
#     search_fields = ['name', 'description']
#     prepopulated_fields = {'slug': ('name',)}
    
#     class Media:
#         js = (
#             'http://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js',
#             'modeltranslation/js/tabbed_translation_fields.js',
#         )
#         css = {
#             'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
#         }


# @admin.register(Tag)
# class TagAdmin(TranslationAdmin):
#     list_display = ['name', 'slug', 'created_at']
#     search_fields = ['name']
#     prepopulated_fields = {'slug': ('name',)}


# @admin.register(Post)
# class PostAdmin(TranslationAdmin):
#     list_display = ['title', 'author', 'category', 'status', 'published_at', 'read_time']
#     list_filter = ['status', 'category', 'tags', 'created_at', 'published_at']
#     search_fields = ['title', 'content', 'excerpt']
#     prepopulated_fields = {'slug': ('title',)}
#     filter_horizontal = ['tags']
#     date_hierarchy = 'published_at'
    
#     fieldsets = (
#         ('Basic Information', {
#             'fields': ('title', 'slug', 'author', 'category', 'tags', 'status')
#         }),
#         ('Content (English)', {
#             'fields': ('title_en', 'excerpt_en', 'content_en'),
#             'classes': ('collapse',)
#         }),
#         ('Content (Persian)', {
#             'fields': ('title_fa', 'excerpt_fa', 'content_fa'),
#             'classes': ('collapse',)
#         }),
#         ('SEO (English)', {
#             'fields': ('meta_description_en', 'meta_keywords_en'),
#             'classes': ('collapse',)
#         }),
#         ('SEO (Persian)', {
#             'fields': ('meta_description_fa', 'meta_keywords_fa'),
#             'classes': ('collapse',)
#         }),
#         ('Media & Metadata', {
#             'fields': ('featured_image', 'published_at', 'read_time')
#         }),
#     )
    
#     def save_model(self, request, obj, form, change):
#         if not obj.author_id:
#             obj.author = request.user
#         super().save_model(request, obj, form, change)


# @admin.register(Project)
# class ProjectAdmin(TranslationAdmin):
#     list_display = ['title', 'featured', 'order', 'created_at']
#     list_filter = ['featured', 'tags']
#     search_fields = ['title', 'description']
#     prepopulated_fields = {'slug': ('title',)}
#     filter_horizontal = ['tags']
#     list_editable = ['featured', 'order']
    
#     fieldsets = (
#         ('Basic Information', {
#             'fields': ('title', 'slug', 'tags', 'featured', 'order')
#         }),
#         ('Content (English)', {
#             'fields': ('title_en', 'description_en'),
#             'classes': ('collapse',)
#         }),
#         ('Content (Persian)', {
#             'fields': ('title_fa', 'description_fa'),
#             'classes': ('collapse',)
#         }),
#         ('Links & Media', {
#             'fields': ('github_url', 'demo_url', 'image')
#         }),
#     )