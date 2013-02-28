"""Factories for the ``multilingual_events`` app."""
from django.utils.timezone import now

import factory

from ..models import Event, EventCategory, EventCategoryTitle, EventTitle


class EventCategoryFactory(factory.Factory):
    """Factory for the ``EventCategory`` model."""
    FACTORY_FOR = EventCategory

    slug = factory.Sequence(lambda n: 'category-{0}'.format(n))


class EventCategoryTitleENFactory(factory.Factory):
    """Factory for the ``EventCategoryTitle`` model. Language is English."""
    FACTORY_FOR = EventCategoryTitle

    title = 'Category title'
    category = factory.SubFactory(EventCategoryFactory)
    language = 'en'


class EventCategoryTitleDEFactory(factory.Factory):
    """Factory for the ``EventCategoryTitle`` model. Language is German."""
    FACTORY_FOR = EventCategoryTitle

    title = 'Kategorie Titel'
    category = factory.SubFactory(EventCategoryFactory)
    language = 'de'


class EventFactory(factory.Factory):
    """Factory for the ``Event`` model."""
    FACTORY_FOR = Event

    start_date = factory.LazyAttribute(lambda x: now())
    is_published = True


class EventTitleENFactory(factory.Factory):
    """Factory for the ``EventTitle`` model. Language is English."""
    FACTORY_FOR = EventTitle

    title = 'A title'
    description = 'A description'
    event = factory.SubFactory(EventFactory)
    language = 'en'


class EventTitleDEFactory(factory.Factory):
    """Factory for the ``EventTitle`` model. Language is German."""
    FACTORY_FOR = EventTitle

    title = 'Ein Titel'
    description = 'Eine Beschreibung'
    event = factory.SubFactory(EventFactory)
    language = 'de'
