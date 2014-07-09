"""Sitemaps for the `multilingual_news` app."""
from django.contrib.sitemaps import Sitemap

from multilingual_events.models import Event


class EventSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Event.objects.all()

    def lastmod(self, obj):
        return obj.creation_date
