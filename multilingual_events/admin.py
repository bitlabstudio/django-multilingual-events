"""Admin classes for the ``multilingual_event`` app."""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from parler.admin import TranslatableAdmin

from .models import Event, EventCategory


class EventCategoryAdmin(TranslatableAdmin):
    """Admin class for the ``EventCategory`` model."""
    list_display = ['get_title', 'all_languages_column', ]
    list_select_related = []

    def get_title(self, obj):
        return obj.title
    get_title.short_description = _('Title')


class EventAdmin(TranslatableAdmin):
    """Admin class for the ``Event`` model."""
    list_display = ['get_title', 'start_date', 'user', 'all_languages_column',
                    'get_is_published']
    list_select_related = []

    def get_title(self, obj):
        return obj.title
    get_title.short_description = _('Title')

    def get_is_published(self, obj):
        return obj.is_published
    get_is_published.short_description = _('Is published')
    get_is_published.boolean = True


admin.site.register(Event, EventAdmin)
admin.site.register(EventCategory, EventCategoryAdmin)
