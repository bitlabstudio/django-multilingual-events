"""Factories for the ``multilingual_events`` app."""
from django.utils.timezone import now

import factory
from django_libs.tests.factories import HvadFactoryMixin

from ..models import (
    Event,
    EventCategory,
    EventPluginModel,
)


class EventCategoryFactory(HvadFactoryMixin, factory.DjangoModelFactory):
    """Factory for the ``EventCategory`` model."""
    FACTORY_FOR = EventCategory

    slug = factory.Sequence(lambda n: 'category-{0}'.format(n))
    title = 'Category title'


class EventFactory(HvadFactoryMixin, factory.DjangoModelFactory):
    """Factory for the ``Event`` model."""
    FACTORY_FOR = Event

    category = factory.SubFactory(EventCategoryFactory)
    start_date = factory.LazyAttribute(lambda x: now())
    title = 'A title'
    description = 'A description'
    is_published = True


class EventPluginModelFactory(factory.DjangoModelFactory):
    """Factory for ``EventPluginModel`` objects."""
    FACTORY_FOR = EventPluginModel

    display_type = 'small'
    event = factory.SubFactory(EventFactory)
