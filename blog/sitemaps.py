from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'
    i18n = True
    alternates = True
    x_default = True

    def items(self):
        return ['blog:index', 'blog:about', 'blog:resume', 'blog:services',
                'blog:portfolio', 'blog:blog_list', 'blog:contact']

    def location(self, item):
        return reverse(item)


class PostSitemap(Sitemap):
    priority = 0.9
    changefreq = 'monthly'
    i18n = True
    alternates = True
    x_default = True

    def items(self):
        return Post.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at
