Django Multilingual Events
==========================

An app for collecting information about events and agendas.

This could be useful for e.g. conventions, meetings etc.


Installation
------------

Prerequisites:

* Django
* django-hvad
* django-cms (tested with v3 beta)
* django-document-library

If you want to install the latest stable release from PyPi::

    $ pip install django-multilingual-events

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/django-multilingual-events.git#egg=multilingual_events

Add ``multilingnual_events`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'document_library',
        'easy_thumbnails',
        'filer',
        'hvad',
        'multilingual_events',
        'cms',
    )

Run the migrations::

    ./manage.py migrate multilingual_events


Usage
-----

Using the apphook
+++++++++++++++++

Simply create a django-cms page and select ``Multilingual Events Apphook`` in
the ``Application`` field of the ``Advanced Settings``.

Settings
--------

EVENT_PAGINATION
++++++++++++++++

Default: 20

Define a pagination amount for the event listing.


Sitemaps
++++++++

To add a sitemap of your events, add the following to your urlconf: ::

    from multilingual_events.sitemaps import EventSitemap

    urlpatterns += patterns(
        '',
        url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {
            'sitemaps': {
                'events': EventSitemap,
            }, }),
    )


Roadmap
-------

Check the issue tracker on github for milestones and features to come.
