Django Multilingual Events 
==========================

TODO: Describe app


Installation
------------

Prerequisites:

* Django
* simple-translation
* django-cms
* cmsplugin-blog
* django-document-library
* TODO: Is that all?

If you want to install the latest stable release from PyPi::

    $ pip install django-multilingual-events

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/django-multilingual-events.git#egg=multilingual_events

Add ``multilingnual_events`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'multilingual_events',
    )

Run the South migrations::

    ./manage.py migrate multilingual_events 


Usage
-----

TODO: Describe usage


Roadmap
-------

Check the issue tracker on github for milestones and features to come.
