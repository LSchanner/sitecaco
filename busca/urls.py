from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.BuscaView),
    # Busca em uma das três cartegorias  (FALTA IMPLEMENTAR E TESTAR)
    url(r'^(?P<tipo>(ata|pagina|noticia))/(?P<pag>[0-9]*)$', views.BuscaCartegoriaView),
]
