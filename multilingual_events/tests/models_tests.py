"""Tests for the models of the ``multilingual_events`` app."""
from django.test import TestCase
from django.utils import timezone

from ..models import Event
from .factories import EventFactory, EventTitleFactory


class EventManagerTestCase(TestCase):
    """Tests for the ``EventManager`` class."""
    longMessage = True

    def test_get_visible(self):
        manager = Event.objects

        # the following two events should be visible
        # a visible event
        EventFactory()

        # a past event with future end date
        past = timezone.now() - timezone.timedelta(1)
        future = timezone.now() + timezone.timedelta(1)
        EventFactory(start_date=past, end_date=future)

        # the following two events should be invisible
        # an invisible event
        EventFactory(is_published=False)

        # a past event
        past = timezone.now() - timezone.timedelta(1)
        EventFactory(start_date=past)

        result = manager.get_visible()
        self.assertEqual(result.count(), 2)


class EventTestCase(TestCase):
    """Tests for the ``Event`` model class."""
    longMessage = True

    def test_model(self):
        instance = EventFactory()
        self.assertTrue(instance.pk, msg=(
            'Should be able to instantiate and save the model.'))


class EventTitleTestCase(TestCase):
    """Tests for the ``EventTitle`` model class."""
    longMessage = True

    def test_model(self):
        instance = EventTitleFactory()
        self.assertTrue(instance.pk, msg=(
            'Should be able to instantiate and save the model.'))
