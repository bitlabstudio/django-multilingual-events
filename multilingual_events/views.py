"""Views for the ``multilingual_events`` app."""
from django.views.generic import DetailView, TemplateView

from .models import Event


class EventListView(TemplateView):
    """A view that lists all upcoming events for the current language."""
    template_name = 'multilingual_events/event_list.html'

    def get_context_data(self, **kwargs):
        ctx = super(EventListView, self).get_context_data(**kwargs)

        upcoming = Event.objects.get_upcoming(self.request)
        archived = Event.objects.get_archived(self.request)

        ctx.update({
            'upcoming_events': upcoming,
            'archived_events': archived,
        })
        return ctx


class EventDetailView(DetailView):
    """A view that displays detailed information about an event."""
    model = Event
