# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Distrito'
        db.create_table(u'Localizacion_distrito', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'Localizacion', ['Distrito'])

        # Adding M2M table for field Trabajos on 'Distrito'
        m2m_table_name = db.shorten_name(u'Localizacion_distrito_Trabajos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('distrito', models.ForeignKey(orm[u'Localizacion.distrito'], null=False)),
            ('trabajosencillo', models.ForeignKey(orm[u'Trabajos.trabajosencillo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['distrito_id', 'trabajosencillo_id'])

        # Adding M2M table for field Proyectos on 'Distrito'
        m2m_table_name = db.shorten_name(u'Localizacion_distrito_Proyectos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('distrito', models.ForeignKey(orm[u'Localizacion.distrito'], null=False)),
            ('proyecto', models.ForeignKey(orm[u'Trabajos.proyecto'], null=False))
        ))
        db.create_unique(m2m_table_name, ['distrito_id', 'proyecto_id'])

        # Adding model 'Provincia'
        db.create_table(u'Localizacion_provincia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'Localizacion', ['Provincia'])

        # Adding M2M table for field Distritos on 'Provincia'
        m2m_table_name = db.shorten_name(u'Localizacion_provincia_Distritos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('provincia', models.ForeignKey(orm[u'Localizacion.provincia'], null=False)),
            ('distrito', models.ForeignKey(orm[u'Localizacion.distrito'], null=False))
        ))
        db.create_unique(m2m_table_name, ['provincia_id', 'distrito_id'])


    def backwards(self, orm):
        # Deleting model 'Distrito'
        db.delete_table(u'Localizacion_distrito')

        # Removing M2M table for field Trabajos on 'Distrito'
        db.delete_table(db.shorten_name(u'Localizacion_distrito_Trabajos'))

        # Removing M2M table for field Proyectos on 'Distrito'
        db.delete_table(db.shorten_name(u'Localizacion_distrito_Proyectos'))

        # Deleting model 'Provincia'
        db.delete_table(u'Localizacion_provincia')

        # Removing M2M table for field Distritos on 'Provincia'
        db.delete_table(db.shorten_name(u'Localizacion_provincia_Distritos'))


    models = {
        u'Localizacion.distrito': {
            'Meta': {'object_name': 'Distrito'},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Proyectos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Trabajos.Proyecto']", 'symmetrical': 'False'}),
            'Trabajos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Trabajos.TrabajoSencillo']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Localizacion.provincia': {
            'Distritos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Localizacion.Distrito']", 'symmetrical': 'False'}),
            'Meta': {'object_name': 'Provincia'},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Maquinas.maquina': {
            'Meta': {'object_name': 'Maquina'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'Trabajos.proyecto': {
            'Autor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Usuarios.Autor']"}),
            'Descripcion': ('django.db.models.fields.TextField', [], {}),
            'EquipoNecesario': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Maquinas.Maquina']", 'symmetrical': 'False'}),
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
            'Localizacion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Meta': {'object_name': 'TrabajoSencillo'},
            'Titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Usuarios.autor': {
            'Meta': {'object_name': 'Autor'},
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['Localizacion']