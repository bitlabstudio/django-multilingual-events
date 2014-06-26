# -*- coding: utf-8 -*-
"""Tests for the models of the ``multilingual_events`` app."""
from __future__ import unicode_literals

from mock import Mock
from django.test import TestCase
from django.utils import timezone

from ..models import Event
from .factories import EventFactory, EventPluginModelFactory


class EventManagerTestCase(TestCase):
    """Tests for the ``EventManager`` class."""
    longMessage = True

    def setUp(self):
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

    def test_get_visible_and_get_archived(self):
        manager = Event.objects

        request = Mock(LANGUAGE_CODE='en')
        result = manager.get_upcoming(request)
        self.assertEqual(result.count(), 2)

        result = manager.get_archived(request)
        self.assertEqual(result.count(), 1)

        # another past event
        past = timezone.now() - timezone.timedelta(1)
        EventFactory(start_date=past)

        result = manager.get_archived(request)
        self.assertEqual(result.count(), 2)


class EventTestCase(TestCase):
    """Tests for the ``Event`` model class."""
    longMessage = True

    def setUp(self):
        self.event = EventFactory()

    def test_model(self):
        self.assertTrue(self.event.pk, msg=(
            'Should be able to instantiate and save the model.'))

    def test_get_address(self):
        self.assertEqual(self.event.get_address(), '', msg=(
            'Should return an empty address.'))
        self.event.venue_name = 'Foo'
        self.event.address_1 = 'Bar'
        self.event.address_2 = 'Foo'
        self.event.city = 'Bar'
        self.event.postal_code = '12345'
        self.assertEqual(self.event.get_address(),
                         'Foo<br />Bar<br />Foo<br />12345 Bar<br />',
                         msg=('Should return a formatted address.'))

    def test_get_alternative_events(self):
        self.assertEqual(len(self.event.get_alternative_events()), 0, msg=(
            'Should return an empty list of alternative events.'))

    def test_get_city_and_country(self):
        self.assertEqual(self.event.get_city_and_country(), '', msg=(
            'Should return an empty string.'))
        self.event.city = 'Bar'
        self.assertEqual(self.event.get_city_and_country(), 'Bar, ', msg=(
            'Should return the city.'))

    def test_get_number_of_days(self):
        self.assertEqual(self.event.get_number_of_days(), 1, msg=(
            'Should return the duration of one day.'))
        self.event.end_date = timezone.now() + timezone.timedelta(2)
        self.assertEqual(self.event.get_number_of_days(), 3, msg=(
            'Should return the duration of three days.'))


class EventPluginModelTestCase(TestCase):
    """Tests for the ``EventPluginModel`` model."""
    longMessage = True

    def test_model(self):
        obj = EventPluginModelFactory()
        self.assertTrue(obj.pk, msg=(
            'Should be able to instantiate and save the model.'))
