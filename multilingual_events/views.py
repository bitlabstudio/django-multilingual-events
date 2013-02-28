"""Views for the ``multilingual_events`` app."""
from django.views.generic import DetailView, TemplateView
from django.utils import timezone

from simple_translation.middleware import filter_queryset_language

from .models import Event


class EventListView(TemplateView):
    """A view that lists all upcoming events for the current language."""
    template_name = 'multilingual_events/event_list.html'

    def get_context_data(self, **kwargs):
        ctx = super(EventListView, self).get_context_data(**kwargs)

        yesterday = timezone.now().date() - timezone.timedelta(1)

        qs = Event.objects.filter(is_published=True)
        qs = qs.filter(start_date__gte=yesterday)
        upcoming = filter_queryset_language(self.request, qs)

        qs = Event.objects.filter(is_published=True)
        qs = qs.filter(start_date__lt=yesterday)
        archived = filter_queryset_language(self.request, qs)
        return {
            'upcoming_events': upcoming,
            'archived_events': archived,
        }


class EventDetailView(DetailView):
    """A view that displays detailed information about an event."""
    model = Event
