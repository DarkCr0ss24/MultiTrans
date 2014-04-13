# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Maquina'
        db.create_table(u'Maquinas_maquina', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'Maquinas', ['Maquina'])


    def backwards(self, orm):
        # Deleting model 'Maquina'
        db.delete_table(u'Maquinas_maquina')


    models = {
        u'Maquinas.maquina': {
            'Meta': {'object_name': 'Maquina'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['Maquinas']