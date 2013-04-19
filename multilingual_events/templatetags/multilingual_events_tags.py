"""Templatetags for the ``multilingual_events`` app."""
from django import template

from ..models import EventCategory, Event


register = template.Library()


@register.assignment_tag
def get_event_categories():
    """Returns all categories in the database."""
    return EventCategory.objects.all().order_by('position')


@register.assignment_tag(takes_context=True)
def get_events(context, amount=5):
    """
    Returns upcoming and currently running events.

    :param request: The current request.
    :param amount: The number of events that should be returned.

    """
    request = context.get('request')
    qs = Event.objects.get_upcoming(request)
    if not qs.count():
        return qs
    return qs[:amount]
