# -*- coding: utf-8 -*-
"""Tests for the models of the ``multilingual_events`` app."""
from __future__ import unicode_literals

from mock import Mock
from django.test import TestCase
from django.utils import timezone

from mixer.backend.django import mixer

from ..models import Event


class EventManagerTestCase(TestCase):
    """Tests for the ``EventManager`` class."""
    longMessage = True

    def setUp(self):
        past = timezone.now() - timezone.timedelta(1)
        future = timezone.now() + timezone.timedelta(1)

        # the following two events should be visible
        # a visible event
        event = mixer.blend('multilingual_events.EventTranslation',
                            is_published=True, language_code='en',
                            start_date=future).master
        event.is_published = True
        event.start_date = future
        event.save()

        # a past event with future end date
        mixer.blend('multilingual_events.EventTranslation',
                    language_code='en', start_date=past, end_date=future)

        # the following two events should be invisible
        # an invisible event
        mixer.blend('multilingual_events.EventTranslation', is_published=False)

        # a past event
        event = mixer.blend('multilingual_events.EventTranslation',
                            is_published=True, language_code='en',
                            start_date=past).master
        event.is_published = True
        event.start_date = past
        event.save()

    def test_get_visible_and_get_archived(self):
        manager = Event.objects

        request = Mock(LANGUAGE_CODE='en')
        result = manager.get_upcoming(request)
        self.assertEqual(result.count(), 1)

        result = manager.get_archived(request)
        self.assertEqual(result.count(), 1)


class EventTestCase(TestCase):
    """Tests for the ``Event`` model class."""
    longMessage = True

    def setUp(self):
        self.event = mixer.blend('multilingual_events.EventTranslation',
                                 language_code='en').master

    def test_model(self):
        self.assertTrue(self.event.pk, msg=(
            'Should be able to instantiate and save the model.'))

    def test_get_address(self):
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
        self.event.city = 'Bar'
        self.assertEqual(self.event.get_city_and_country(), 'Bar, ', msg=(
            'Should return the city.'))

    def test_get_number_of_days(self):
        self.assertEqual(self.event.get_number_of_days(), 1, msg=(
            'Should return the duration of one day.'))
        self.event.start_date = timezone.now() - timezone.timedelta(1)
        self.event.end_date = timezone.now() + timezone.timedelta(1)
        self.assertEqual(self.event.get_number_of_days(), 3, msg=(
            'Should return the duration of three days.'))


class EventPluginModelTestCase(TestCase):
    """Tests for the ``EventPluginModel`` model."""
    longMessage = True

    def test_model(self):
        obj = mixer.blend('multilingual_events.EventPluginModel')
        self.assertTrue(obj.pk, msg=(
            'Should be able to instantiate and save the model.'))
