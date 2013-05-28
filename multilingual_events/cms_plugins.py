"""CMS plugins for the ``multilingual_events`` app."""
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from .forms import EventAgendaSessionForm, EventAgendaTalkForm
from .models import (
    EventAgendaDay,
    EventAgendaSession,
    EventAgendaTalk,
    EventPluginModel,
)


class EventAgendaDayPlugin(CMSPluginBase):
    """CMS plugin for the ``EventAgendaDay`` model."""
    model = EventAgendaDay
    name = _('Event Agenda Day')
    render_template = 'multilingual_events/plugins/event_agenda_day.html'

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context


class EventAgendaSessionPlugin(CMSPluginBase):
    """CMS plugin for the ``EventAgendaSession`` model."""
    model = EventAgendaSession
    form = EventAgendaSessionForm
    name = _('Event Agenda Session')
    render_template = 'multilingual_events/plugins/event_agenda_session.html'

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context


class EventAgendaTalkPlugin(CMSPluginBase):
    """CMS plugin for the ``EventAgendaTalk`` model."""
    model = EventAgendaTalk
    form = EventAgendaTalkForm
    name = _('Event Agenda Talk')
    render_template = 'multilingual_events/plugins/event_agenda_talk.html'

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context


class EventPlugin(CMSPluginBase):
    model = EventPluginModel
    name = _('Event Plugin')
    render_template = 'multilingual_events/event_plugin.html'

    def render(self, context, instance, placeholder):
        context.update({
            'plugin': instance,
            'event': instance.event,
        })
        return context


plugin_pool.register_plugin(EventAgendaDayPlugin)
plugin_pool.register_plugin(EventAgendaSessionPlugin)
plugin_pool.register_plugin(EventAgendaTalkPlugin)
plugin_pool.register_plugin(EventPlugin)
