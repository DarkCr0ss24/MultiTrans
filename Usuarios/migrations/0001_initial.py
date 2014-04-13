# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Usuario'
        db.create_table(u'Usuarios_usuario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('correo', self.gf('django.db.models.fields.EmailField')(max_length=50)),
            ('clave', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'Usuarios', ['Usuario'])

        # Adding model 'Autor'
        db.create_table(u'Usuarios_autor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('correo', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'Usuarios', ['Autor'])


    def backwards(self, orm):
        # Deleting model 'Usuario'
        db.delete_table(u'Usuarios_usuario')

        # Deleting model 'Autor'
        db.delete_table(u'Usuarios_autor')


    models = {
        u'Usuarios.autor': {
            'Meta': {'object_name': 'Autor'},
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'Usuarios.usuario': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Usuario'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'clave': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['Usuarios']