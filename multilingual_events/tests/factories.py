"""Factories for the ``multilingual_events`` app."""
from django.utils.timezone import now

import factory
from django_libs.tests.factories import SimpleTranslationMixin

from ..models import (
    Event,
    EventCategory,
    EventCategoryTitle,
    EventTitle,
    EventPluginModel,
)


class EventCategoryFactory(SimpleTranslationMixin, factory.Factory):
    """Factory for the ``EventCategory`` model."""
    FACTORY_FOR = EventCategory

    slug = factory.Sequence(lambda n: 'category-{0}'.format(n))

    @staticmethod
    def _get_translation_factory_and_field():
        return (EventCategoryTitleFactory, 'category')


class EventCategoryTitleFactory(factory.Factory):
    """Factory for the ``EventCategoryTitle`` model."""
    FACTORY_FOR = EventCategoryTitle

    title = 'Category title'
    category = factory.SubFactory(EventCategoryFactory)
    language = 'en'


class BaseEventFactory(factory.Factory):
    """Factory for the ``Event`` model."""
    FACTORY_FOR = Event

    category = factory.SubFactory(EventCategoryFactory)
    start_date = factory.LazyAttribute(lambda x: now())


class EventFactory(SimpleTranslationMixin, BaseEventFactory):
    FACTORY_FOR = Event

    @staticmethod
    def _get_translation_factory_and_field():
        return (EventTitleFactory, 'event')


class EventPluginModelFactory(factory.Factory):
    """Factory for ``EventPluginModel`` objects."""
    FACTORY_FOR = EventPluginModel

    display_type = 'small'
    event = factory.SubFactory(EventFactory)


class EventTitleFactory(factory.Factory):
    """Factory for the ``EventTitle`` model."""
    FACTORY_FOR = EventTitle

    title = 'A title'
    description = 'A description'
    # we use only the BaseEventFactory here, because calling the EventFactory
    # as SubFactory will result in duplicate EventTitle objects
    event = factory.SubFactory(BaseEventFactory)
    language = 'en'
    is_published = True
