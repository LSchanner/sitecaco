from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.BuscaView),
    url(r'^\/(?P<tipo>(ata|pagina|noticia))(/(?P<pag>[0-9]*))?$', views.BuscaCartegoriaView),
]
