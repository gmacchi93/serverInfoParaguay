from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from views import *

router = DefaultRouter()
router.register(r'categorias' ,CategoriaViewSet)
router.register(r'negocios',NegocioViewSet,base_name='negocio')
router.register(r'sugerencias',SugerenciasViewSet)
router.register(r'noticias',NoticiasViewSet)
router.register(r'sugerencias',SugerenciasViewSet)

urlpatterns = patterns('core.api.views',
	url(r'^api/',include(router.urls)),
    )