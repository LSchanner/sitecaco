from django.conf.urls import patterns, include, url
from django.contrib import admin
import sitecaco.views as views
from django.conf import settings
from haystack.query import SearchQuerySet
from haystack.views import SearchView


urlpatterns = patterns('',

    #urls do site
    url(r'^$',views.HomeView),
    url(r'^institucional/$' ,views.InstitucionalView),
    url(r'^eventos/$' ,views.EventosView),
    url(r'^servicos/$' ,views.ServicosView),
    url(r'^institucional/atas/(?P<pag>[0-9]*)' ,views.AtasView),
    url(r'^institucional/ata/(?P<id>[0-9]*)' ,views.AtaView),
    url(r'^noticias/(?P<pag>[0-9]*)', views.NoticiasView),
    url(r'^noticia/(?P<id>[0-9]*)', views.NoticiaView),
    url(r'^produtos/(?P<id>[0-9]*)' ,views.ProdutosView),

    #Banco de Provas
    url('^bancodeprovas',views.BancoView),

    #Busca em atas,páginas e notícias
    url(r'^busca$',views.BuscaView),

    #Busca em uma das três cartegorias
    url(r'^busca/(?P<tipo>(ata|pagina|noticia))/(?P<pag>[0-9]*)$',views.BuscaCartegoriaView),

    #urls da interface de admin
    url(r'^admin/', include(admin.site.urls)),
    )


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
    )


