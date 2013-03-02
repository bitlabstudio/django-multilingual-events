"""Tests for the templatetags of the ``multilingual_events`` app."""
from django.template import RequestContext
from django.test import TestCase, RequestFactory

from ..templatetags.multilingual_events_tags import get_events
from .factories import EventFactory


class GetEventsTestCase(TestCase):
    """Tests for the ``get_events`` templatetag."""
    def test_tag(self):
        EventFactory()
        EventFactory()
        req = RequestFactory().get('/')
        context = RequestContext(req)
        result = get_events(context)
        self.assertEqual(result.count(), 2)
