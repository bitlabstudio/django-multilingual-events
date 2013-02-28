"""Registering translated models for the ``multilingual_events`` app."""
from simple_translation.translation_pool import translation_pool

from . import models


translation_pool.register_translation(
    models.EventCategory, models.EventCategoryTitle)
translation_pool.register_translation(models.Event, models.EventTitle)
