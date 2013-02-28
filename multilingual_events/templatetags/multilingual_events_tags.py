"""Templatetags for the ``simple_events`` app."""
from django import template

from simple_translation.middleware import filter_queryset_language

from ..models import EventCategory, EventTitle


register = template.Library()


@register.assignment_tag
def get_event_categories():
    """Returns all categories in the database."""
    return EventCategory.objects.all().order_by('position')


@register.assignment_tag(takes_context=True)
def get_events(context, amount=5):
    """
    Returns upcoming events.

    :param request: The current request.
    :param amount: The number of events that should be returned.

    """
    request = context.get('request')
    qs = EventTitle.objects.filter(
        event__is_published=True).order_by('event__start_date')
    qs = filter_queryset_language(request, qs)
    return qs[:amount]
