"""Tests for the templatetags of the ``multilingual_events`` app."""
from django.template import RequestContext
from django.test import TestCase, RequestFactory

from ..templatetags.multilingual_events_tags import (
    get_events,
    get_event_categories,
)
from .factories import EventFactory, EventCategoryFactory


class GetEventsTestCase(TestCase):
    """Tests for the ``get_events`` templatetag."""
    longMessage = True

    def test_tag(self):
        EventFactory()
        EventFactory()
        req = RequestFactory().get('/')
        req.LANGUAGE_CODE = 'en'
        context = RequestContext(req)
        result = get_events(context)
        self.assertEqual(result.count(), 2)

        req.LANGUAGE_CODE = None
        context = RequestContext(req)
        result = get_events(context)
        self.assertEqual(result.count(), 0, msg=(
            'When no LANGUAGE_CODE can be found, it should return an empty'
            ' QuerySet'))


class GetEventCategoriesTestCase(TestCase):
    """Tests for the ``get_event_categories`` templatetag."""
    longMessage = True

    def test_tag(self):
        EventCategoryFactory()
        self.assertEqual(get_event_categories().count(), 1, msg=(
            'Should return one category.'))
