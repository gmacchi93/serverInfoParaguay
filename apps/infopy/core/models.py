# -*- coding: utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
#from __future__ import unicode_literals

from django.db import models


class Activador(models.Model):
    id_esta = models.BigIntegerField(primary_key=True)
    descri = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'activador'


class BuscadorCant(models.Model):
    id_bus = models.BigIntegerField(primary_key=True)
    palabra = models.CharField(max_length=100)
    fecha = models.IntegerField()
    fecha_ver = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'buscador_cant'


class CCiudadanas(models.Model):
    id_cc = models.AutoField(primary_key=True)
    nombre_cc = models.CharField(max_length=200)
    copete_cc = models.CharField(max_length=200, blank=True, null=True)
    texto_cc = models.TextField()
    imagen_cc = models.CharField(max_length=255, blank=True, null=True)
    online = models.CharField(max_length=2)
    local_sugerido = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_ciudadanas'


class Categoria(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombre_cat = models.CharField(max_length=180)
    visitas = models.CharField(max_length=255)
    online = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'categoria'


class Contactenos(models.Model):
    id_contactos = models.AutoField(primary_key=True)
    nombre_contacto = models.CharField(max_length=100)
    apellido_contacto = models.CharField(max_length=200, blank=True, null=True)
    direccion_contacto = models.CharField(max_length=255, blank=True, null=True)
    ciudad_contacto = models.CharField(max_length=255, blank=True, null=True)
    telefono_contacto = models.CharField(max_length=200, blank=True, null=True)
    celular_contacto = models.CharField(max_length=200, blank=True, null=True)
    mail_contacto = models.CharField(max_length=100)
    contactarme_con = models.CharField(max_length=100)
    texto_contacto = models.TextField()
    fecha_contacto = models.DateTimeField()
    respuesta = models.CharField(max_length=2)
    texto_resp = models.TextField(blank=True, null=True)
    fecha_resp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contactenos'


class ContadorVisitas(models.Model):
    id_visitas = models.AutoField(primary_key=True)
    ip_visitante = models.CharField(max_length=100)
    mes_visita = models.CharField(max_length=100)
    anio_visita = models.CharField(max_length=100)
    visitas = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'contador_visitas'


class DetalleTarjeta(models.Model):
    id_tarje = models.BigIntegerField(primary_key=True)
    id_negocio = models.IntegerField()
    estado = models.CharField(max_length=2)
    id_nombre = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_tarjeta'


class Links(models.Model):
    nombre_link = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'links'


class Negocio(models.Model):
    id = models.BigIntegerField(primary_key=True)
    destacado = models.CharField(max_length=2, blank=True, null=True)
    destacar = models.CharField(max_length=2, blank=True, null=True)
    sugerido = models.CharField(max_length=2, blank=True, null=True)
    direccion = models.CharField(max_length=200)
    latitud = models.CharField(max_length=100, blank=True, null=True)
    longitud = models.CharField(max_length=100, blank=True, null=True)
    nombre = models.CharField(max_length=150)
    zona = models.CharField(max_length=100, blank=True, null=True)
    localidad = models.CharField(max_length=100, blank=True, null=True)
    creacion = models.DateTimeField()
    modificacion = models.DateTimeField(blank=True, null=True)
    usuario_id = models.IntegerField()
    ubicacion = models.CharField(max_length=100, blank=True, null=True)
    imagen = models.CharField(max_length=200, blank=True, null=True)
    imagen1 = models.CharField(max_length=255, blank=True, null=True)
    imagen2 = models.CharField(max_length=255, blank=True, null=True)
    imagen3 = models.CharField(max_length=255, blank=True, null=True)
    categoria_id = models.IntegerField()
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    descrip_larga = models.TextField()
    hora_aper = models.CharField(max_length=20, blank=True, null=True)
    hora_cierre = models.CharField(max_length=20, blank=True, null=True)
    tarjeta_cre = models.CharField(max_length=25)
    tarjeta_debi = models.CharField(max_length=25)
    estacionamiento = models.CharField(max_length=2, blank=True, null=True)
    telefono = models.CharField(max_length=40, blank=True, null=True)
    barrio = models.CharField(max_length=80, blank=True, null=True)
    mail = models.CharField(max_length=150, blank=True, null=True)
    web = models.CharField(max_length=180, blank=True, null=True)
    rs1 = models.CharField(max_length=255, blank=True, null=True)
    rs2 = models.CharField(max_length=255, blank=True, null=True)
    rs3 = models.CharField(max_length=255, blank=True, null=True)
    rs4 = models.CharField(max_length=255, blank=True, null=True)
    visitas = models.CharField(max_length=255)
    online = models.CharField(max_length=2)
    nuevo = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'negocio'


class Noticias(models.Model):
    id_noticias = models.AutoField(primary_key=True)
    titulo_noticia = models.CharField(max_length=100)
    copete_noticia = models.CharField(max_length=200)
    texto_noticia = models.TextField()
    imagen_noticia = models.CharField(max_length=100, blank=True, null=True)
    fecha_noticia = models.DateTimeField()
    autor_noticia = models.CharField(max_length=100)
    online = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'noticias'


class Slide(models.Model):
    id_slide = models.AutoField(primary_key=True)
    nombre_slide = models.CharField(max_length=200)
    descrip_slide = models.CharField(max_length=255, blank=True, null=True)
    imagen_slide = models.CharField(max_length=255)
    online = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'slide'


class Sugerencias(models.Model):
    id_sug = models.AutoField(primary_key=True)
    titulo_sug = models.CharField(max_length=200)
    descrip_sug = models.CharField(max_length=200, blank=True, null=True)
    texto_sug = models.TextField()
    imagen_sug = models.CharField(max_length=200, blank=True, null=True)
    fecha_sug = models.DateTimeField(blank=True, null=True)
    online = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'sugerencias'


class Tarjeta(models.Model):
    id_ta = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'tarjeta'


class TipoUsuario(models.Model):
    idtiusu = models.BigIntegerField(primary_key=True)
    descri = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Usuario(models.Model):
    id = models.BigIntegerField(primary_key=True)
    usuario = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=255)  # Field renamed because it was a Python reserved word.
    mail = models.CharField(max_length=100)
    ingreso = models.DateTimeField()
    modificado = models.DateTimeField(blank=True, null=True)
    keyes = models.CharField(max_length=60, blank=True, null=True)
    id_esta = models.IntegerField()
    validado = models.IntegerField()
    idtiusu = models.IntegerField()
    avatar = models.CharField(max_length=100, blank=True, null=True)
    usuario_semana = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class Usuarionegocio(models.Model):
    unid = models.BigIntegerField(primary_key=True)
    negocio_id = models.IntegerField()
    usuario_id = models.IntegerField()
    usuario_fb = models.CharField(max_length=180, blank=True, null=True)
    ip_usuario = models.CharField(max_length=100)
    comentario = models.CharField(max_length=180, blank=True, null=True)
    coment_estado = models.IntegerField(blank=True, null=True)
    visitas_usu = models.IntegerField()
    votos = models.IntegerField()
    media = models.FloatField()
    fecha_create = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'usuarionegocio'


class VotosUsuarios(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario_id = models.IntegerField()
    ip_usuario = models.CharField(max_length=100)
    fecha_voto = models.DateField()

    class Meta:
        managed = False
        db_table = 'votos_usuarios'