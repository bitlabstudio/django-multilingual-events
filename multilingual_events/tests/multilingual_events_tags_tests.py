"""Tests for the templatetags of the ``multilingual_events`` app."""
from django.template import RequestContext
from django.test import TestCase, RequestFactory
from django.utils import timezone

from mixer.backend.django import mixer

from ..templatetags.multilingual_events_tags import (
    get_events,
    get_event_categories,
)


class GetEventsTestCase(TestCase):
    """Tests for the ``get_events`` templatetag."""
    longMessage = True

    def test_tag(self):
        future = timezone.now() + timezone.timedelta(1)

        # the following two events should be visible
        # a visible event
        event = mixer.blend('multilingual_events.EventTranslation',
                            is_published=True, language_code='en',
                            start_date=future).master
        event.is_published = True
        event.start_date = future
        event.save()

        req = RequestFactory().get('/')
        req.LANGUAGE_CODE = 'en'
        context = RequestContext(req)
        result = get_events(context)
        self.assertEqual(result.count(), 1)


class GetEventCategoriesTestCase(TestCase):
    """Tests for the ``get_event_categories`` templatetag."""
    longMessage = True

    def test_tag(self):
        mixer.blend('multilingual_events.EventCategoryTranslation')
        self.assertEqual(get_event_categories().count(), 1, msg=(
            'Should return one category.'))
