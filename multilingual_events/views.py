"""Views for the ``multilingual_events`` app."""
from django.db.models import Q
from django.views.generic import DetailView, ListView
from django.utils import timezone

from .models import Event
from .settings import PAGINATION


class EventListView(ListView):
    """A view that lists all upcoming events for the current language."""
    template_name = 'multilingual_events/event_list.html'

    def get_queryset(self):
        return Event.objects.get_published(self.request)

    def get_context_data(self, **kwargs):
        ctx = super(EventListView, self).get_context_data(**kwargs)
        paginator, page, queryset, is_paginated = self.paginate_queryset(
            self.object_list, PAGINATION)

        events = self.object_list.filter(
            pk__in=list(queryset.values_list('pk', flat=True)))

        upcoming = events.filter(
            Q(end_date__gte=timezone.now()) |
            Q(start_date__gte=timezone.now())).order_by(
            'start_date', 'start_time')
        archived = events.filter(
            Q(start_date__lt=timezone.now()) & (Q(end_date__isnull=True) | Q(
                end_date__lt=timezone.now())))

        ctx.update({
            'paginator': paginator,
            'page_obj': page,
            'is_paginated': is_paginated,
            'object_list': queryset,
            'upcoming_events': upcoming,
            'archived_events': archived,
        })
        return ctx


class EventDetailView(DetailView):
    """A view that displays detailed information about an event."""
    model = Event
