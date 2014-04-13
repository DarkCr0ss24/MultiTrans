# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TrabajoSencillo'
        db.create_table(u'Trabajos_trabajosencillo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Titulo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Autor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Usuarios.Autor'])),
            ('Descripcion', self.gf('django.db.models.fields.TextField')()),
            ('Localizacion', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'Trabajos', ['TrabajoSencillo'])

        # Adding M2M table for field EquipoNecesario on 'TrabajoSencillo'
        m2m_table_name = db.shorten_name(u'Trabajos_trabajosencillo_EquipoNecesario')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('trabajosencillo', models.ForeignKey(orm[u'Trabajos.trabajosencillo'], null=False)),
            ('maquina', models.ForeignKey(orm[u'Maquinas.maquina'], null=False))
        ))
        db.create_unique(m2m_table_name, ['trabajosencillo_id', 'maquina_id'])

        # Adding model 'Proyecto'
        db.create_table(u'Trabajos_proyecto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Titulo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Autor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Usuarios.Autor'])),
            ('Descripcion', self.gf('django.db.models.fields.TextField')()),
            ('Localizacion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('NumeroDeUsuarios', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'Trabajos', ['Proyecto'])

        # Adding M2M table for field EquipoNecesario on 'Proyecto'
        m2m_table_name = db.shorten_name(u'Trabajos_proyecto_EquipoNecesario')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyecto', models.ForeignKey(orm[u'Trabajos.proyecto'], null=False)),
            ('maquina', models.ForeignKey(orm[u'Maquinas.maquina'], null=False))
        ))
        db.create_unique(m2m_table_name, ['proyecto_id', 'maquina_id'])


    def backwards(self, orm):
        # Deleting model 'TrabajoSencillo'
        db.delete_table(u'Trabajos_trabajosencillo')

        # Removing M2M table for field EquipoNecesario on 'TrabajoSencillo'
        db.delete_table(db.shorten_name(u'Trabajos_trabajosencillo_EquipoNecesario'))

        # Deleting model 'Proyecto'
        db.delete_table(u'Trabajos_proyecto')

        # Removing M2M table for field EquipoNecesario on 'Proyecto'
        db.delete_table(db.shorten_name(u'Trabajos_proyecto_EquipoNecesario'))


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

    complete_apps = ['Trabajos']