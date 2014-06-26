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
        'people',
        'cms',
        'mptt',
    )

Run the South migrations::

    ./manage.py migrate multilingual_events


Usage
-----

Using the apphook
+++++++++++++++++

Simply create a django-cms page and select ``Multilingual Events Apphook`` in
the ``Application`` field of the ``Advanced Settings``.


Roadmap
-------

Check the issue tracker on github for milestones and features to come.
