# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activador',
            fields=[
                ('id_esta', models.BigIntegerField(serialize=False, primary_key=True)),
                ('descri', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'activador',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BuscadorCant',
            fields=[
                ('id_bus', models.BigIntegerField(serialize=False, primary_key=True)),
                ('palabra', models.CharField(max_length=100)),
                ('fecha', models.IntegerField()),
                ('fecha_ver', models.DateTimeField()),
            ],
            options={
                'db_table': 'buscador_cant',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('nombre_cat', models.CharField(max_length=180)),
                ('visitas', models.CharField(max_length=255)),
                ('online', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'categoria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CCiudadanas',
            fields=[
                ('id_cc', models.AutoField(serialize=False, primary_key=True)),
                ('nombre_cc', models.CharField(max_length=200)),
                ('copete_cc', models.CharField(max_length=200, null=True, blank=True)),
                ('texto_cc', models.TextField()),
                ('imagen_cc', models.CharField(max_length=255, null=True, blank=True)),
                ('online', models.CharField(max_length=2)),
                ('local_sugerido', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'c_ciudadanas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contactenos',
            fields=[
                ('id_contactos', models.AutoField(serialize=False, primary_key=True)),
                ('nombre_contacto', models.CharField(max_length=100)),
                ('apellido_contacto', models.CharField(max_length=200, null=True, blank=True)),
                ('direccion_contacto', models.CharField(max_length=255, null=True, blank=True)),
                ('ciudad_contacto', models.CharField(max_length=255, null=True, blank=True)),
                ('telefono_contacto', models.CharField(max_length=200, null=True, blank=True)),
                ('celular_contacto', models.CharField(max_length=200, null=True, blank=True)),
                ('mail_contacto', models.CharField(max_length=100)),
                ('contactarme_con', models.CharField(max_length=100)),
                ('texto_contacto', models.TextField()),
                ('fecha_contacto', models.DateTimeField()),
                ('respuesta', models.CharField(max_length=2)),
                ('texto_resp', models.TextField(null=True, blank=True)),
                ('fecha_resp', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'contactenos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ContadorVisitas',
            fields=[
                ('id_visitas', models.AutoField(serialize=False, primary_key=True)),
                ('ip_visitante', models.CharField(max_length=100)),
                ('mes_visita', models.CharField(max_length=100)),
                ('anio_visita', models.CharField(max_length=100)),
                ('visitas', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'contador_visitas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleTarjeta',
            fields=[
                ('id_tarje', models.BigIntegerField(serialize=False, primary_key=True)),
                ('id_negocio', models.IntegerField()),
                ('estado', models.CharField(max_length=2)),
                ('id_nombre', models.IntegerField()),
            ],
            options={
                'db_table': 'detalle_tarjeta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_link', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'links',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Negocio',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('destacado', models.CharField(max_length=2, null=True, blank=True)),
                ('destacar', models.CharField(max_length=2, null=True, blank=True)),
                ('sugerido', models.CharField(max_length=2, null=True, blank=True)),
                ('direccion', models.CharField(max_length=200)),
                ('latitud', models.CharField(max_length=100, null=True, blank=True)),
                ('longitud', models.CharField(max_length=100, null=True, blank=True)),
                ('nombre', models.CharField(max_length=150)),
                ('zona', models.CharField(max_length=100, null=True, blank=True)),
                ('localidad', models.CharField(max_length=100, null=True, blank=True)),
                ('creacion', models.DateTimeField()),
                ('modificacion', models.DateTimeField(null=True, blank=True)),
                ('usuario_id', models.IntegerField()),
                ('ubicacion', models.CharField(max_length=100, null=True, blank=True)),
                ('imagen', models.CharField(max_length=200, null=True, blank=True)),
                ('imagen1', models.CharField(max_length=255, null=True, blank=True)),
                ('imagen2', models.CharField(max_length=255, null=True, blank=True)),
                ('imagen3', models.CharField(max_length=255, null=True, blank=True)),
                ('categoria_id', models.IntegerField()),
                ('descripcion', models.CharField(max_length=255, null=True, blank=True)),
                ('descrip_larga', models.TextField()),
                ('hora_aper', models.CharField(max_length=20, null=True, blank=True)),
                ('hora_cierre', models.CharField(max_length=20, null=True, blank=True)),
                ('tarjeta_cre', models.CharField(max_length=25)),
                ('tarjeta_debi', models.CharField(max_length=25)),
                ('estacionamiento', models.CharField(max_length=2, null=True, blank=True)),
                ('telefono', models.CharField(max_length=40, null=True, blank=True)),
                ('barrio', models.CharField(max_length=80, null=True, blank=True)),
                ('mail', models.CharField(max_length=150, null=True, blank=True)),
                ('web', models.CharField(max_length=180, null=True, blank=True)),
                ('rs1', models.CharField(max_length=255, null=True, blank=True)),
                ('rs2', models.CharField(max_length=255, null=True, blank=True)),
                ('rs3', models.CharField(max_length=255, null=True, blank=True)),
                ('rs4', models.CharField(max_length=255, null=True, blank=True)),
                ('visitas', models.CharField(max_length=255)),
                ('online', models.CharField(max_length=2)),
                ('nuevo', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'negocio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id_noticias', models.AutoField(serialize=False, primary_key=True)),
                ('titulo_noticia', models.CharField(max_length=100)),
                ('copete_noticia', models.CharField(max_length=200)),
                ('texto_noticia', models.TextField()),
                ('imagen_noticia', models.CharField(max_length=100, null=True, blank=True)),
                ('fecha_noticia', models.DateTimeField()),
                ('autor_noticia', models.CharField(max_length=100)),
                ('online', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'noticias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id_slide', models.AutoField(serialize=False, primary_key=True)),
                ('nombre_slide', models.CharField(max_length=200)),
                ('descrip_slide', models.CharField(max_length=255, null=True, blank=True)),
                ('imagen_slide', models.CharField(max_length=255)),
                ('online', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'slide',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sugerencias',
            fields=[
                ('id_sug', models.AutoField(serialize=False, primary_key=True)),
                ('titulo_sug', models.CharField(max_length=200)),
                ('descrip_sug', models.CharField(max_length=200, null=True, blank=True)),
                ('texto_sug', models.TextField()),
                ('imagen_sug', models.CharField(max_length=200, null=True, blank=True)),
                ('fecha_sug', models.DateTimeField(null=True, blank=True)),
                ('online', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'sugerencias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id_ta', models.BigIntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'tarjeta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('idtiusu', models.BigIntegerField(serialize=False, primary_key=True)),
                ('descri', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tipo_usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('usuario', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100, null=True, blank=True)),
                ('apellido', models.CharField(max_length=100, null=True, blank=True)),
                ('pass_field', models.CharField(max_length=255, db_column=b'pass')),
                ('mail', models.CharField(max_length=100)),
                ('ingreso', models.DateTimeField()),
                ('modificado', models.DateTimeField(null=True, blank=True)),
                ('keyes', models.CharField(max_length=60, null=True, blank=True)),
                ('id_esta', models.IntegerField()),
                ('validado', models.IntegerField()),
                ('idtiusu', models.IntegerField()),
                ('avatar', models.CharField(max_length=100, null=True, blank=True)),
                ('usuario_semana', models.CharField(max_length=2, null=True, blank=True)),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuarionegocio',
            fields=[
                ('unid', models.BigIntegerField(serialize=False, primary_key=True)),
                ('negocio_id', models.IntegerField()),
                ('usuario_id', models.IntegerField()),
                ('usuario_fb', models.CharField(max_length=180, null=True, blank=True)),
                ('ip_usuario', models.CharField(max_length=100)),
                ('comentario', models.CharField(max_length=180, null=True, blank=True)),
                ('coment_estado', models.IntegerField(null=True, blank=True)),
                ('visitas_usu', models.IntegerField()),
                ('votos', models.IntegerField()),
                ('media', models.FloatField()),
                ('fecha_create', models.DateTimeField()),
            ],
            options={
                'db_table': 'usuarionegocio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VotosUsuarios',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('usuario_id', models.IntegerField()),
                ('ip_usuario', models.CharField(max_length=100)),
                ('fecha_voto', models.DateField()),
            ],
            options={
                'db_table': 'votos_usuarios',
                'managed': False,
            },
        ),
    ]
