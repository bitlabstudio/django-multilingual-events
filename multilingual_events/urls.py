"""URLs for the ``multilingual_events`` app."""
from django.conf.urls.defaults import patterns, url

from simple_events.views import (
    EventDetailView,
    EventListView,
)


urlpatterns = patterns(
    '',
    url(r'^$',
        EventListView.as_view(),
        name='simple_events_list'),

    url(r'^(?P<pk>\d+)/$',
        EventDetailView.as_view(),
        name='simple_events_detail'),
)
