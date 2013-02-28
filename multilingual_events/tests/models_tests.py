"""Tests for the models of the ``multilingual_events`` app."""
from django.test import TestCase

from .factories import (
    EventCategoryTitleENFactory,
    EventFactory,
    EventTitleENFactory,
)


class EventTestCase(TestCase):
    """Tests for the ``Event`` model class."""
    longMessage = True

    def test_model(self):
        cat_en = EventCategoryTitleENFactory()
        instance = EventFactory(category=cat_en.category)
        self.assertTrue(instance.pk, msg=(
            'Should be able to instantiate and save the model.'))


class EventTitleTestCase(TestCase):
    """Tests for the ``EventTitle`` model class."""
    longMessage = True

    def test_model(self):
        cat_en = EventCategoryTitleENFactory()
        instance = EventTitleENFactory(event__category=cat_en.category)
        self.assertTrue(instance.pk, msg=(
            'Should be able to instantiate and save the model.'))
