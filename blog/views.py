"""
Views for blog with bilingual support.
"""

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.utils.translation import get_language
from django.db.models import Q
from .models import Post, Project, Category, Tag


class HomeView(ListView):
    """Homepage with latest posts."""
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_queryset(self):
        return Post.objects.filter(status='published').select_related('author', 'category').prefetch_related('tags')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_posts'] = Post.objects.filter(
            status='published'
        ).select_related('author', 'category')[:3]
        context['current_language'] = get_language()
        return context


class PostDetailView(DetailView):
    """Individual post detail page."""
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Post.objects.filter(status='published').select_related('author', 'category').prefetch_related('tags')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_language'] = get_language()
        
        # Related posts from same category
        context['related_posts'] = Post.objects.filter(
            category=self.object.category,
            status='published'
        ).exclude(id=self.object.id)[:3]
        
        return context


class CategoryPostsView(ListView):
    """Posts filtered by category."""
    model = Post
    template_name = 'blog/category_posts.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(
            category=self.category,
            status='published'
        ).select_related('author', 'category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['current_language'] = get_language()
        return context


class TagPostsView(ListView):
    """Posts filtered by tag."""
    model = Post
    template_name = 'blog/tag_posts.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return Post.objects.filter(
            tags=self.tag,
            status='published'
        ).select_related('author', 'category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        context['current_language'] = get_language()
        return context


class ProjectListView(ListView):
    """Portfolio projects page."""
    model = Project
    template_name = 'blog/projects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.prefetch_related('tags')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_language'] = get_language()
        return context


class ProjectDetailView(DetailView):
    """Individual project detail."""
    model = Project
    template_name = 'blog/project_detail.html'
    context_object_name = 'project'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_language'] = get_language()
        return context


class SearchView(ListView):
    """Search posts."""
    model = Post
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(excerpt__icontains=query),
                status='published'
            ).select_related('author', 'category')
        return Post.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['current_language'] = get_language()
        return context