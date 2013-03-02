"""Factories for the ``multilingual_events`` app."""
from django.utils.timezone import now

import factory
from django_libs.tests.factories import SimpleTranslationMixin

from ..models import Event, EventCategory, EventCategoryTitle, EventTitle


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


class EventFactory(SimpleTranslationMixin, factory.Factory):
    """Factory for the ``Event`` model."""
    FACTORY_FOR = Event

    category = factory.SubFactory(EventCategoryFactory)
    start_date = factory.LazyAttribute(lambda x: now())
    is_published = True

    @staticmethod
    def _get_translation_factory_and_field():
        return (EventTitleFactory, 'event')


class EventTitleFactory(factory.Factory):
    """Factory for the ``EventTitle`` model."""
    FACTORY_FOR = EventTitle

    title = 'A title'
    description = 'A description'
    event = factory.SubFactory(EventFactory)
    language = 'en'
