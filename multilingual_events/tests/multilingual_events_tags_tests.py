"""Tests for the templatetags of the ``multilingual_events`` app."""
from django.template import RequestContext
from django.test import TestCase, RequestFactory

from ..templatetags.multilingual_events_tags import get_events
from .factories import (
    EventCategoryTitleDEFactory,
    EventCategoryTitleENFactory,
    EventTitleDEFactory,
    EventTitleENFactory,
)


class GetEventsTestCase(TestCase):
    """Tests for the ``get_events`` templatetag."""
    def setUp(self):
        super(GetEventsTestCase, self).setUp()
        cat_en = EventCategoryTitleENFactory()
        cat_de = EventCategoryTitleDEFactory()

        EventTitleENFactory(event__category=cat_en.category)
        EventTitleENFactory(event__category=cat_en.category)
        EventTitleENFactory(event__category=cat_en.category)
        EventTitleENFactory(event__category=cat_en.category)
        EventTitleENFactory(event__category=cat_en.category)

        EventTitleDEFactory(event__category=cat_de.category)
        EventTitleDEFactory(event__category=cat_de.category)

    def test_tag(self):
        req = RequestFactory().get('/')
        context = RequestContext(req)
        result = get_events(context)
        self.assertEqual(result.count(), 5)
        for event in result:
            self.assertEqual(event.language, 'en')
