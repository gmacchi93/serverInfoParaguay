from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework import generics
from serializers import *
from ..models import *
from rest_framework import permissions



# Create your views here.
class ActivadorViewSet(ModelViewSet):
    serializer_class = ActivadorSerializer
    queryset = Activador.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class BuscadorCantViewSet(ModelViewSet):
    serializer_class = BuscadorCantSerializer
    queryset = BuscadorCant.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CCiudadanasViewSet(ModelViewSet):
    serializer_class = CCiudadanasSerializer
    queryset = CCiudadanas.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CategoriaViewSet(ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ContactenosViewSet(ModelViewSet):
    serializer_class = ContactenosSerializer
    queryset = Contactenos.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ContadorVisitasViewSet(ModelViewSet):
    serializer_class = ContadorVisitasSerializer
    queryset = ContadorVisitas.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class DetalleTarjetaViewSet(ModelViewSet):
    serializer_class = DetalleTarjetaSerializer
    queryset = DetalleTarjeta.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class LinksViewSet(ModelViewSet):
    serializer_class = LinksSerializer
    queryset = Links.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class NegocioViewSet(ModelViewSet):
    serializer_class = NegocioSerializer
    def get_queryset(self):
        queryset = Negocio.objects.all()
        categoria_id = self.request.QUERY_PARAMS.get('categoria_id', None)
        if categoria_id is not None:
            queryset = queryset.filter(categoria_id=categoria_id)
        return queryset
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class NoticiasViewSet(ModelViewSet):
    serializer_class = NoticiasSerializer
    queryset = Noticias.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SlideViewSet(ModelViewSet):
    serializer_class = SlideSerializer
    queryset = Slide.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SugerenciasViewSet(ModelViewSet):
    serializer_class = SugerenciasSerializer
    queryset = Sugerencias.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class TarjetaViewSet(ModelViewSet):
    serializer_class = TarjetaSerializer
    queryset = Tarjeta.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class TipoUsuarioViewSet(ModelViewSet):
    serializer_class = TipoUsuarioSerializer
    queryset = TipoUsuario.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UsuarioViewSet(ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UsuarionegocioViewSet(ModelViewSet):
    serializer_class = UsuarionegocioSerializer
    queryset = Usuarionegocio.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class TipoUsuarioViewSet(ModelViewSet):
    serializer_class = TipoUsuarioSerializer
    queryset = TipoUsuario.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

