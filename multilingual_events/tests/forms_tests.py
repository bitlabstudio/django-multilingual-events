"""Tests for the forms of the ``multilingual_events`` app."""
from django.test import TestCase


class EventAgendaSessionFormTestCase(TestCase):
    """Tests for the ``EventAgendaSessionForm`` form class."""
    longMessage = True

    def test_form(self):
        from ..forms import EventAgendaSessionForm
        form = EventAgendaSessionForm()
        self.assertFalse(form.is_valid(), msg='The form should not be valid.')
