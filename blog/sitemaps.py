from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'weekly'

    def items(self):
        return ['blog:index', 'blog:about', 'blog:resume', 'blog:services', 'blog:portfolio', 'blog:contact']

    def location(self, item):
        return reverse(item)

    def lastmod(self, item):
        # می‌تونی تاریخ آخرین تغییر رو برگردونی
        from datetime import datetime
        return datetime.now()