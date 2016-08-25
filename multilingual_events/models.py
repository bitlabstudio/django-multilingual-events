"""Models for the ``multilingual_events`` app."""
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.translation import get_language, ugettext_lazy as _

from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField
from django_countries.fields import CountryField
from filer.fields.image import FilerImageField
from hvad.models import TranslatedFields, TranslatableModel, TranslationManager

from .settings import DISPLAY_TYPE_CHOICES


lat_lng_help_text = _(
    'You can figure out latitude and longitude at'
    ' <a href="http://universimmedia.pagesperso-orange.fr/geo/loc.htm"'
    ' target="_blank">this website</a>')


class EventCategory(TranslatableModel):
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

    translations = TranslatedFields(
        title=models.CharField(
            max_length=256,
            verbose_name=_('Title'),
        )
    )

    class Meta:
        ordering = ('slug', )
        verbose_name = _('Event Category')
        verbose_name_plural = _('Event Categories')

    def __unicode__(self):
        return self.safe_translation_getter('title', self.slug)


class EventManager(TranslationManager):
    """Custom manager for the ``Event`` model."""
    def get_published(self, request):
        language = getattr(request, 'LANGUAGE_CODE', get_language())
        if not language:
            return self.model.objects.none()

        qs = self.get_queryset()
        qs = qs.filter(
            translations__is_published=True,
            translations__language_code=language,
        )
        return qs.distinct()

    def get_archived(self, request):
        language = getattr(request, 'LANGUAGE_CODE', get_language())
        if not language:
            return self.model.objects.none()

        qs = self.get_queryset()
        qs = qs.filter(
            translations__is_published=True,
            translations__language_code=language,
        )
        qs = qs.filter(
            Q(start_date__lt=timezone.now()) & (
                Q(end_date__isnull=True) | Q(end_date__lt=timezone.now())))
        return qs.distinct()

    def get_upcoming(self, request):
        language = getattr(request, 'LANGUAGE_CODE', get_language())
        if not language:
            return self.model.objects.none()

        qs = self.get_queryset().order_by('start_date', 'start_time')
        qs = qs.filter(
            translations__is_published=True,
            translations__language_code=language,
        )
        qs = qs.filter(
            Q(end_date__gte=timezone.now()) |
            Q(start_date__gte=timezone.now()))
        return qs.distinct()


class Event(TranslatableModel):
    """
    An event is something that happens on a specific start date.

    For translateable fields see ``EventTitle``.

    :start_date: The DateTime when this event starts.
    :creation_date: The DateTime when this event was created.
    :user: The user who created this event.

    """

    conference = PlaceholderField(
        'multilingual_events_conference',
        related_name='conference_events',
    )

    detailed_description = PlaceholderField(
        'multilingual_events_detailed_description',
        related_name='description_events',
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

    image = FilerImageField(
        verbose_name=_('Image'),
        null=True, blank=True,
    )

    translations = TranslatedFields(
        title=models.CharField(
            max_length=512,
            verbose_name=_('Title'),
        ),
        venue_name=models.CharField(
            max_length=256,
            verbose_name=_('Venue name'),
            blank=True,
        ),
        city=models.CharField(
            max_length=256,
            verbose_name=_('City'),
            blank=True,
        ),
        postal_code=models.CharField(
            max_length=256,
            verbose_name=_('Postal code'),
            blank=True,
        ),
        address_1=models.CharField(
            max_length=256,
            verbose_name=_('Address 1'),
            blank=True,
        ),
        address_2=models.CharField(
            max_length=256,
            verbose_name=_('Address 2'),
            blank=True,
        ),
        room=models.CharField(
            max_length=256,
            verbose_name=_('Block / Room'),
            blank=True,
        ),
        description=models.TextField(
            verbose_name=_('Description'),
            blank=True,
        ),
        is_published=models.BooleanField(
            default=False,
            verbose_name=_('Is published'),
        ),
        meta_description=models.TextField(
            max_length=512,
            verbose_name=_('Meta description'),
            blank=True,
        )
    )

    objects = EventManager()

    class Meta:
        ordering = ('-start_date', '-start_time')
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __unicode__(self):
        return self.safe_translation_getter('title', 'Event on the {0}'.format(
            self.start_date))

    def get_absolute_url(self):
        return reverse('multilingual_events_detail', kwargs={'pk': self.pk})

    def get_address(self):
        """Returns the address with country."""
        full_address = u''
        if self.venue_name:
            full_address += u'{0}<br />'.format(self.venue_name)
        if self.address_1:
            full_address += u'{0}<br />'.format(self.address_1)
        if self.address_2:
            full_address += u'{0}<br />'.format(self.address_2)
        if self.city:
            if self.postal_code:
                full_address += u'{0} '.format(self.postal_code)
            full_address += u'{0}<br />'.format(self.city)
        full_address += u'{0}'.format(unicode(self.country.name))
        return full_address

    def get_alternative_events(self):
        return Event.objects.filter(category=self.category).exclude(
            pk=self.pk).order_by('start_date')

    def get_city_and_country(self):
        result = u''
        if self.city:
            result += u'{0}, '.format(self.city)
        result += unicode(self.country.name)
        return result

    def get_number_of_days(self):
        """Returns the number of days for this event."""
        if not self.end_date:
            return 1
        amount = self.end_date - self.start_date
        return amount.days + 1


class EventPluginModel(CMSPlugin):
    """
    Model for the ``EventPlugin`` cms plugin.

    :display_type: The way the plugin is displayed. E.g. 'big' or 'small'
    :event: The event this plugin shows.

    """
    display_type = models.CharField(
        max_length=256,
        choices=DISPLAY_TYPE_CHOICES,
        verbose_name=_('Display type'),
    )
    event = models.ForeignKey(
        Event,
        verbose_name=_('Event'),
    )

    def __unicode__(self):
        return '{} ({})'.format(self.event, self.event.category)


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
