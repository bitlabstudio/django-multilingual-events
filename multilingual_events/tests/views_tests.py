"""Tests for the views of the ``multilingual_events`` app."""
from django.test import TestCase, RequestFactory

from mixer.backend.django import mixer
from ..views import EventDetailView, EventListView


class EventListViewTestCase(TestCase):
    """Tests for the ``EventListView`` view class."""
    def test_view(self):
        req = RequestFactory().get('/')
        resp = EventListView.as_view()(req)
        self.assertEqual(resp.status_code, 200)


class EventDetailViewTestCase(TestCase):
    """Tests for the ``EventDetailView`` view class."""
    def test_view(self):
        event = mixer.blend('multilingual_events.EventTranslation')
        req = RequestFactory().get('/')
        resp = EventDetailView.as_view()(req, pk=event.pk)
        self.assertEqual(resp.status_code, 200)
