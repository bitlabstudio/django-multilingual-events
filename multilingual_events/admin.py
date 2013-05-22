"""Admin classes for the ``multilingual_event`` app."""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from cmsplugin_blog.admin import M2MPlaceholderAdmin
from django_libs.admin import MultilingualPublishMixin
from simple_translation.admin import TranslationAdmin

from .models import Event, EventCategory


class EventCategoryAdmin(TranslationAdmin):
    """Admin class for the ``EventCategory`` model."""
    list_display = ['title', 'languages', ]

    def title(self, obj):
        return obj.get_translation().title
    title.short_description = _('Title')


class EventAdmin(MultilingualPublishMixin, M2MPlaceholderAdmin):
    """Admin class for the ``Event`` model."""
    list_display = ['title', 'start_date', 'user', 'languages', 'is_published']

    def title(self, obj):
        return obj.get_translation().title
    title.short_description = _('Title')


admin.site.register(Event, EventAdmin)
admin.site.register(EventCategory, EventCategoryAdmin)
