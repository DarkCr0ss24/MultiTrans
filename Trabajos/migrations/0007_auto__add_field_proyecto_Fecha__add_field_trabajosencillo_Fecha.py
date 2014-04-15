# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Proyecto.Fecha'
        db.add_column(u'Trabajos_proyecto', 'Fecha',
                      self.gf('django.db.models.fields.DateField')(auto_now=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'TrabajoSencillo.Fecha'
        db.add_column(u'Trabajos_trabajosencillo', 'Fecha',
                      self.gf('django.db.models.fields.DateField')(auto_now=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Proyecto.Fecha'
        db.delete_column(u'Trabajos_proyecto', 'Fecha')

        # Deleting field 'TrabajoSencillo.Fecha'
        db.delete_column(u'Trabajos_trabajosencillo', 'Fecha')


    models = {
        u'Maquinas.maquina': {
            'Meta': {'object_name': 'Maquina'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'Trabajos.proyecto': {
            'Autor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Usuarios.Autor']"}),
            'Descripcion': ('django.db.models.fields.TextField', [], {}),
            'EquipoNecesario': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Maquinas.Maquina']", 'symmetrical': 'False'}),
            'Fecha': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'Localizacion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Meta': {'object_name': 'Proyecto'},
            'NumeroDeUsuarios': ('django.db.models.fields.IntegerField', [], {}),
            'Titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Trabajos.trabajosencillo': {
            'Autor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Usuarios.Autor']"}),
            'Descripcion': ('django.db.models.fields.TextField', [], {}),
            'EquipoNecesario': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Maquinas.Maquina']", 'symmetrical': 'False'}),
            'Fecha': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'Localizacion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Meta': {'object_name': 'TrabajoSencillo'},
            'Titulo': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Usuarios.autor': {
            'Meta': {'object_name': 'Autor'},
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['Trabajos']