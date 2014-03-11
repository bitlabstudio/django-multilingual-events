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

    def test_model(self):
        instance = EventFactory()
        self.assertTrue(instance.pk, msg=(
            'Should be able to instantiate and save the model.'))


class EventPluginModelTestCase(TestCase):
    """Tests for the ``EventPluginModel`` model."""
    longMessage = True

    def test_model(self):
        obj = EventPluginModelFactory()
        self.assertTrue(obj.pk, msg=(
            'Should be able to instantiate and save the model.'))
