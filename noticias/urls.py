from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^\/(?P<id>[0-9]*)', views.NoticiaView, name="Noticia"),
    url(r'^s\/(?P<pag>[0-9]*)', views.NoticiasView, name="Noticias"),
]
