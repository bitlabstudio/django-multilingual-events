"""URLs for the ``multilingual_events`` app."""

from django.urls import re_path

from .views import EventDetailView, EventListView


urlpatterns = [
    re_path(r"^$", EventListView.as_view(), name="multilingual_events_list"),
    re_path(
        r"^(?P<pk>\d+)/$", EventDetailView.as_view(), name="multilingual_events_detail"
    ),
]
