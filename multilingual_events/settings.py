"""Settings for the ``multilingual_events`` app."""
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


display_type_choices = [
    ('small', _('small')),
    ('big', _('big')),
]

DISPLAY_TYPE_CHOICES = getattr(
    settings, 'EVENT_PLUGIN_DISPLAY_TYPE_CHOICES', display_type_choices)
