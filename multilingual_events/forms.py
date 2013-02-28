"""Forms for the ``multilingual_events`` app."""
from django.contrib import admin
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from django.forms.models import ModelForm

from .models import EventAgendaSession, EventAgendaTalk


class EventAgendaAdminWithDocumentMixin(object):
    """
    Mixin for cms plugins that have a FK to ``document_library.Document``.

    """
    def __init__(self, *args, **kwargs):
        super(EventAgendaAdminWithDocumentMixin, self).__init__(
            *args, **kwargs)
        self.fields['document'].widget = ForeignKeyRawIdWidget(
            self._meta.model._meta.get_field('document').rel, admin.site,
        )


class EventAgendaSessionForm(EventAgendaAdminWithDocumentMixin, ModelForm):
    """Admin form for the ``EventAgendaSession`` plugin."""
    class Meta:
        model = EventAgendaSession


class EventAgendaTalkForm(EventAgendaAdminWithDocumentMixin, ModelForm):
    """Admin form for the ``EventAgendaSession`` plugin."""
    class Meta:
        model = EventAgendaTalk
