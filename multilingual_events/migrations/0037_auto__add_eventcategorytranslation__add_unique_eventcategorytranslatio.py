# flake8: noqa
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EventCategoryTranslation'
        db.create_table('multilingual_events_eventcategory_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['multilingual_events.EventCategory'])),
        ))
        db.send_create_signal('multilingual_events', ['EventCategoryTranslation'])

        # Adding unique constraint on 'EventCategoryTranslation', fields ['language_code', 'master']
        db.create_unique('multilingual_events_eventcategory_translation', ['language_code', 'master_id'])

        # Adding model 'EventTranslation'
        db.create_table('multilingual_events_event_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('venue_name', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('address_1', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('address_2', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('room', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('meta_description', self.gf('django.db.models.fields.TextField')(max_length=512, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['multilingual_events.Event'])),
        ))
        db.send_create_signal('multilingual_events', ['EventTranslation'])

        # Adding unique constraint on 'EventTranslation', fields ['language_code', 'master']
        db.create_unique('multilingual_events_event_translation', ['language_code', 'master_id'])

        # Adding field 'Event.conference'
        db.add_column('multilingual_events_event', 'conference',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'conference_events', null=True, to=orm['cms.Placeholder']),
                      keep_default=False)

        # Adding field 'Event.detailed_description'
        db.add_column('multilingual_events_event', 'detailed_description',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'description_events', null=True, to=orm['cms.Placeholder']),
                      keep_default=False)


    def backwards(self, orm):
        # Removing unique constraint on 'EventTranslation', fields ['language_code', 'master']
        db.delete_unique('multilingual_events_event_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'EventCategoryTranslation', fields ['language_code', 'master']
        db.delete_unique('multilingual_events_eventcategory_translation', ['language_code', 'master_id'])

        # Deleting model 'EventCategoryTranslation'
        db.delete_table('multilingual_events_eventcategory_translation')

        # Deleting model 'EventTranslation'
        db.delete_table('multilingual_events_event_translation')

        # Deleting field 'Event.conference'
        db.delete_column('multilingual_events_event', 'conference_id')

        # Deleting field 'Event.detailed_description'
        db.delete_column('multilingual_events_event', 'detailed_description_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 13, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'document_library.document': {
            'Meta': {'ordering': "(u'position', u'-creation_date')", 'object_name': 'Document'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['document_library.DocumentCategory']", 'null': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'document_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'download_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_on_front_page': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'placeholders': ('djangocms_utils.fields.M2MPlaceholderField', [], {'to': "orm['cms.Placeholder']", 'symmetrical': 'False'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'source_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'document_library.documentcategory': {
            'Meta': {'object_name': 'DocumentCategory'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '32'})
        },
        'multilingual_events.event': {
            'Meta': {'ordering': "(u'start_date',)", 'object_name': 'Event'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['multilingual_events.EventCategory']"}),
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'conference_events'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'detailed_description': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'description_events'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lng': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'placeholders': ('djangocms_utils.fields.M2MPlaceholderField', [], {'to': "orm['cms.Placeholder']", 'symmetrical': 'False'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'start_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'timezone': ('django.db.models.fields.CharField', [], {'max_length': '65', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'url_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'venue_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'multilingual_events.eventagendaday': {
            'Meta': {'object_name': 'EventAgendaDay', 'db_table': "'cmsplugin_eventagendaday'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'multilingual_events.eventagendasession': {
            'Meta': {'object_name': 'EventAgendaSession', 'db_table': "'cmsplugin_eventagendasession'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '4000', 'blank': 'True'}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['document_library.Document']", 'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'multilingual_events.eventagendatalk': {
            'Meta': {'object_name': 'EventAgendaTalk', 'db_table': "'cmsplugin_eventagendatalk'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '4000', 'blank': 'True'}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['document_library.Document']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'multilingual_events.eventcategory': {
            'Meta': {'object_name': 'EventCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'multilingual_events.eventcategorytitle': {
            'Meta': {'object_name': 'EventCategoryTitle'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['multilingual_events.EventCategory']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'multilingual_events.eventcategorytranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'EventCategoryTranslation', 'db_table': "'multilingual_events_eventcategory_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['multilingual_events.EventCategory']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'multilingual_events.eventpluginmodel': {
            'Meta': {'object_name': 'EventPluginModel', 'db_table': "'cmsplugin_eventpluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'display_type': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['multilingual_events.Event']"})
        },
        'multilingual_events.eventtitle': {
            'Meta': {'object_name': 'EventTitle'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['multilingual_events.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'max_length': '512', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'venue_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        },
        'multilingual_events.eventtranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'EventTranslation', 'db_table': "'multilingual_events_event_translation'"},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['multilingual_events.Event']"}),
            'meta_description': ('django.db.models.fields.TextField', [], {'max_length': '512', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'venue_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        }
    }

    complete_apps = ['multilingual_events']
