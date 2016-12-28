from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from haystack.query import SearchQuerySet
from haystack.views import SearchView


# Para gerar uma página de 404 e 500 diferenciada
handler404 = 'sitecaco.views.page_not_found'
handler500 = 'sitecaco.views.server_error'

urlpatterns = []

# Para quando os path MEDIA e STATIC quando rodar localmente
# https://docs.djangoproject.com/en/1.10/howto/static-files/
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns do projeto - todos são direcionadas aos respe
urlpatterns += [
    # Redireciona para o app institucional
    url(r'^institucional', include('institucional.urls')),
    # Redireciona para o app de Noticias e um id de noticia
    url(r'^noticia', include('noticias.urls')),
    # Redireciona para o app Loja
    url(r'^produtos', include('loja.urls')),
    # Ouvidoria (FALTA IMPLEMENTAR E TESTAR)
    url(r'^contato', include('ouvidoria.urls')),
    # Redireciona para o app Banco de Provas
    url(r'^bancodeprovas', include('banco_de_provas.urls')),
    # Banco de Livros
    url(r'^bancodelivros', include('banco_de_livros.urls')),
    # FISL
    url(r'^eventos/fisl/', include('fisl.urls')),
    # Busca em atas,páginas e notícias (FALTA IMPLEMENTAR E TESTAR)
    # url(r'^busca/$', busca.BuscaView),
    # Busca em uma das três cartegorias  (FALTA IMPLEMENTAR E TESTAR)
    # url(r'^busca/(?P<tipo>(ata|pagina|noticia))/(?P<pag>[0-9]*)$', busca.BuscaCartegoriaView),

    # URLs da interface de admin
    url(r'^admin\/?', admin.site.urls),

    # Redirecionamento para páginas (Como sao mais abrangentes ficam por ultimo)
    url(r'', include('paginas.urls')),
]
