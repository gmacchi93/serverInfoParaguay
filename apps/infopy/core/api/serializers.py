from rest_framework.serializers import ModelSerializer
from ..models import *

class ActivadorSerializer(ModelSerializer):
    class Meta:
        model = Activador
        fields = ('id_esta','descri')

class BuscadorCantSerializer(ModelSerializer):

    class Meta:
        model = BuscadorCant
        fields = ('id_bus','palabra','fecha','fecha_ver')

class CCiudadanasSerializer(ModelSerializer):

    class Meta:
        model = CCiudadanas
        fields = ('id_cc','nombre_cc','copete_cc','texto_cc', 'imagen_cc', 'online','local_sugerido')

class CategoriaSerializer(ModelSerializer):

    class Meta:
        model = Categoria
        fields = ('id','nombre_cat','visitas','online')

class ContactenosSerializer(ModelSerializer):

    class Meta:
        model = Contactenos
        fields = ('id_contactos','nombre_contacto','apellido_contacto','direccion_contacto',
                  'ciudad_contacto','telefono_contacto','celular_contacto','mail_contacto',
                  'contactarme_con','texto_contacto','fecha_contacto','respuesta','texto_resp','fecha_resp')

class ContadorVisitasSerializer(ModelSerializer):

    class Meta:
        model = ContadorVisitas
        fields = ('id_visitas','ip_visitante','mes_visita','anio_visita','visitas')

class DetalleTarjetaSerializer(ModelSerializer):

    class Meta:
        model = DetalleTarjeta
        fields = ('id_tarje','id_negocio','estado','id_nombre')

class LinksSerializer(ModelSerializer):

    class Meta:
        model = Links
        fields = ('nombre_link','link')

class NegocioSerializer(ModelSerializer):

    class Meta:
        model = Negocio
        fields = ('id','destacado','destacar','sugerido','direccion','latitud','longitud','nombre','zona','localidad'
                  ,'creacion','modificacion','usuario_id','ubicacion','imagen','imagen1','imagen2','imagen3','categoria_id'
                  ,'descripcion','descrip_larga','hora_aper','hora_cierre','tarjeta_cre','tarjeta_debi','estacionamiento'
                  ,'telefono','barrio','mail','web','rs1','rs2','rs3','rs4','visitas','online','nuevo')


class NoticiasSerializer(ModelSerializer):

    class Meta:
        model = Noticias
        fields = ('id_noticias','titulo_noticia','copete_noticia','texto_noticia','imagen_noticia','fecha_noticia','autor_noticia','online')

class SlideSerializer(ModelSerializer):

    class Meta:
        model = Slide
        fields = ('id_slide','nombre_slide','descrip_slide','imagen_slide','online')

class SugerenciasSerializer(ModelSerializer):

    class Meta:
        model = Sugerencias
        fields = ('id_sug','titulo_sug','descrip_sug','texto_sug','imagen_sug','fecha_sug','online')

class TarjetaSerializer(ModelSerializer):

    class Meta:
        model = Tarjeta
        fields = ('id_ta','nombre')

class TipoUsuarioSerializer(ModelSerializer):

    class Meta:
        model = TipoUsuario
        fields = ('idtiusu','descri')

class UsuarioSerializer(ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('id','usuario','nombre','apellido','pass_field','mail','ingreso','modificado','keyes','id_esta','validado','idtiusu','avatar','usuario_semana')

class UsuarionegocioSerializer(ModelSerializer):

    class Meta:
        model = TipoUsuario
        fields = ('unid','negocio_id','usuario_id','usuario_fb','ip_usuario','comentario','coment_estado','visitas_usu','votos','media','fecha_create')

class TipoUsuarioSerializer(ModelSerializer):

    class Meta:
        model = TipoUsuario
        fields = ('id','usuario_id','ip_usuario','fecha_voto')

