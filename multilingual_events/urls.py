"""URLs for the ``multilingual_events`` app."""
from django.conf.urls import url

from .views import EventDetailView, EventListView


urlpatterns = [
    url(r'^$',
        EventListView.as_view(),
        name='multilingual_events_list'),

    url(r'^(?P<pk>\d+)/$',
        EventDetailView.as_view(),
        name='multilingual_events_detail'),
]
