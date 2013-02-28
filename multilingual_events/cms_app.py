"""CMS apphook for the ``multilingual_events`` app."""
from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class SimpleEventsApphook(CMSApp):
    name = _("Multilingual Events Apphook")
    urls = ["multilingual_events.urls"]


apphook_pool.register(SimpleEventsApphook)
