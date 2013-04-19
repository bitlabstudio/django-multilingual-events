"""Tests for the templatetags of the ``multilingual_events`` app."""
from django.template import RequestContext
from django.test import TestCase, RequestFactory

from ..templatetags.multilingual_events_tags import get_events
from .factories import EventTitleFactory


class GetEventsTestCase(TestCase):
    """Tests for the ``get_events`` templatetag."""
    longMessage = True

    def test_tag(self):
        EventTitleFactory()
        EventTitleFactory()
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
