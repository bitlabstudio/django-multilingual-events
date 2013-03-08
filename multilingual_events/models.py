"""Models for the ``multilingual_events`` app."""
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.translation import get_language
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from django_countries import CountryField
from django_libs.models_mixins import SimpleTranslationMixin
from djangocms_utils.fields import M2MPlaceholderField
from simple_translation.actions import SimpleTranslationPlaceholderActions
from simple_translation.utils import get_preferred_translation_from_lang


lat_lng_help_text = _(
    'You can figure out latitude and longitude at'
    ' <a href="http://universimmedia.pagesperso-orange.fr/geo/loc.htm"'
    ' target="_blank">this website</a>')


class EventCategory(SimpleTranslationMixin, models.Model):
    """
    Events are grouped in categories.

    For translateable fields see ``EventCategoryTitle``.

    :position: Use this if you want to change the ordering of categories.

    """
    position = models.PositiveIntegerField(
        verbose_name=_('Position'),
        null=True, blank=True,
    )

    slug = models.CharField(
        max_length=32,
        verbose_name=_('Slug'),
    )

    def __unicode__(self):
        return self.get_translation().title


class EventCategoryTitle(models.Model):
    """
    Translateable fields of the ``EventCategory`` model.

    """
    title = models.CharField(
        max_length=256,
        verbose_name=_('Title'),
    )

    # Needed by simple-translation
    category = models.ForeignKey(EventCategory, verbose_name=_('Category'))
    language = models.CharField(max_length=2, verbose_name=_('Language'))


class EventManager(models.Manager):
    """Custom manager for the ``Event`` model."""
    def get_visible(self):
        qs = self.get_query_set()
        qs = qs.filter(is_published=True)
        qs = qs.filter(
            Q(start_date__gte=timezone.now()) |
            Q(end_date__gte=timezone.now()))
        return qs


class Event(SimpleTranslationMixin, models.Model):
    """
    An event is something that happens on a specific start date.

    For translateable fields see ``EventTitle``.

    :start_date: The DateTime when this event starts.
    :is_published: If ``True``, the event would be returned by the
      ``get_events`` templatetag.
    :creation_date: The DateTime when this event was created.
    :user: The user who created this event.

    """

    placeholders = M2MPlaceholderField(
        actions=SimpleTranslationPlaceholderActions(),
        placeholders=('conference', ),
    )

    # Allow null for once but remove this later, when data is setup.
    category = models.ForeignKey(
        EventCategory,
        verbose_name=_('Category'),
    )

    start_date = models.DateField(
        verbose_name=_('Start date'),
    )

    start_time = models.TimeField(
        verbose_name=_('Start time'),
        null=True, blank=True,
    )

    end_date = models.DateField(
        verbose_name=_('End date'),
        null=True, blank=True
    )

    end_time = models.TimeField(
        verbose_name=_('End time'),
        null=True, blank=True,
    )

    timezone = models.CharField(
        max_length=65,
        verbose_name=_('Timezone'),
        blank=True,
    )

    url = models.URLField(
        verbose_name=_('External URL'),
        blank=True,
    )

    url_name = models.CharField(
        max_length=256,
        verbose_name=_('External URL name'),
        blank=True,
    )

    venue_url = models.URLField(
        verbose_name=_('Venue URL'),
        blank=True,
    )

    lat = models.FloatField(
        verbose_name=_('Latitude'),
        help_text=lat_lng_help_text,
        null=True, blank=True,
    )

    lng = models.FloatField(
        verbose_name=_('Longitude'),
        help_text=lat_lng_help_text,
        null=True, blank=True,
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name=_('Is published'),
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=('Creation date'),
    )

    last_update = models.DateTimeField(
        auto_now=True,
    )

    user = models.ForeignKey(
        'auth.User',
        verbose_name=_('User'),
        null=True, blank=True,
    )

    country = CountryField(
        verbose_name=_('Country'),
        null=True, blank=True,
    )

    objects = EventManager()

    class Meta:
        ordering = ('start_date', )

    def __unicode__(self):
        return self.get_title()

    def get_address(self):
        """Returns the address with country."""
        trans = self.get_translation()
        full_address = u''
        if trans.venue_name:
            full_address += u'{0}<br />'.format(trans.venue_name)
        if trans.address_1:
            full_address += u'{0}<br />'.format(trans.address_1)
        if trans.address_2:
            full_address += u'{0}<br />'.format(trans.address_2)
        if trans.city:
            if trans.postal_code:
                full_address += u'{0} '.format(trans.postal_code)
            full_address += u'{0}<br />'.format(trans.city)
        full_address += u'{0}'.format(self.country.name.encode())
        return full_address

    def get_alternative_events(self):
        return Event.objects.filter(category=self.category).exclude(
            pk=self.pk).order_by('start_date')

    def get_city_and_country(self):
        trans = self.get_translation()
        result = u''
        if trans.city:
            result += u'{0}, '.format(trans.city)
        result += self.country.name.encode()
        return result

    def get_number_of_days(self):
        """Returns the number of days for this event."""
        if not self.end_date:
            return 1
        amount = self.end_date - self.start_date
        return amount.days + 1

    def get_title(self):
        lang = get_language()
        return get_preferred_translation_from_lang(self, lang).title


class EventTitle(models.Model):
    """
    Translateable fields of the ``Event`` model.

    """
    title = models.CharField(
        max_length=512,
        verbose_name=_('Title'),
    )

    venue_name = models.CharField(
        max_length=256,
        verbose_name=_('Venue name'),
        blank=True,
    )

    city = models.CharField(
        max_length=256,
        verbose_name=_('City'),
        blank=True,
    )

    postal_code = models.CharField(
        max_length=256,
        verbose_name=_('Postal code'),
        blank=True,
    )

    address_1 = models.CharField(
        max_length=256,
        verbose_name=_('Address 1'),
        blank=True,
    )

    address_2 = models.CharField(
        max_length=256,
        verbose_name=_('Address 2'),
        blank=True,
    )

    room = models.CharField(
        max_length=256,
        verbose_name=_('Block / Room'),
        blank=True,
    )

    description = models.TextField(
        verbose_name=_('Description'),
        blank=True,
    )

    # Needed by simple_translation
    event = models.ForeignKey(Event, verbose_name=_('Event'))
    language = models.CharField(max_length=5, verbose_name=('Language'))

    def get_absolute_url(self):
        middleware = (
            'simple_translation.middleware.MultilingualGenericsMiddleware')
        language_namespace = middleware in settings.MIDDLEWARE_CLASSES \
            and '%s:' % self.language or ''
        return reverse(
            '%smultilingual_events_detail' % language_namespace,
            args=(),
            kwargs={'pk': self.event.pk, }
        )


class EventAgendaDay(CMSPlugin):
    """The day and title of an event."""
    date = models.DateField(
        verbose_name=_('Date'),
    )

    title = models.CharField(
        max_length=256,
        verbose_name=_('Title'),
    )

    def __unicode__(self):
        return self.title


class EventAgendaSession(CMSPlugin):
    """A day can consist of several sessions."""
    start_time = models.DateTimeField(
        verbose_name=_('Start time'),
    )

    end_time = models.DateTimeField(
        verbose_name=_('End time'),
    )

    title = models.CharField(
        max_length=256,
        verbose_name=_('Title'),
    )

    description = models.TextField(
        max_length=4000,
        verbose_name=_('Description'),
        blank=True,
    )

    document = models.ForeignKey(
        'document_library.Document',
        verbose_name=_('Document'),
        null=True, blank=True,
    )


class EventAgendaTalk(CMSPlugin):
    """A session can have several talks."""
    title = models.CharField(
        max_length=256,
        verbose_name=_('Title'),
    )

    description = models.TextField(
        max_length=4000,
        verbose_name=_('Description'),
        blank=True,
    )

    document = models.ForeignKey(
        'document_library.Document',
        verbose_name=_('Document'),
        null=True, blank=True,
    )
