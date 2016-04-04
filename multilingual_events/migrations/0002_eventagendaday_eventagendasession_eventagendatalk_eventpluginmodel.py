# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document_library', '0001_initial'),
        ('cms', '0013_urlconfrevision'),
        ('multilingual_events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventAgendaDay',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('date', models.DateField(verbose_name='Date')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='EventAgendaSession',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('start_time', models.DateTimeField(verbose_name='Start time')),
                ('end_time', models.DateTimeField(verbose_name='End time')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('description', models.TextField(max_length=4000, verbose_name='Description', blank=True)),
                ('document', models.ForeignKey(verbose_name='Document', blank=True, to='document_library.Document', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='EventAgendaTalk',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('description', models.TextField(max_length=4000, verbose_name='Description', blank=True)),
                ('document', models.ForeignKey(verbose_name='Document', blank=True, to='document_library.Document', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='EventPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('display_type', models.CharField(max_length=256, verbose_name='Display type', choices=[(b'small', 'small'), (b'big', 'big')])),
                ('event', models.ForeignKey(verbose_name='Event', to='multilingual_events.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
