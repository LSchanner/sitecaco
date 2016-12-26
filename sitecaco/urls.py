from django.conf.urls import url
from django.contrib import admin

from django.conf import settings
from haystack.query import SearchQuerySet
from haystack.views import SearchView

#Todas as views estão contidas nesse módulo
from sitecaco.views import *

urlpatterns = [
    #urls do site
    url(r'^$', cms.HomeView),
    url(r'^institucional/$', cms.InstitucionalView),
    url(r'^eventos/$', cms.EventosView),
    url(r'^servicos/$', cms.ServicosView),
    url(r'^institucional/atas/(?P<pag>[0-9]*)', cms.AtasView),
    url(r'^institucional/ata/(?P<id>[0-9]*)', cms.AtaView),
    url(r'^noticias/(?P<pag>[0-9]*)', cms.NoticiasView),
    url(r'^noticia/(?P<id>[0-9]*)', cms.NoticiaView),
    url(r'^produtos/(?P<id>[0-9]*)', cms.ProdutosView),

    #Banco de Provas
    url('^bancodeprovas/enviar', banco_provas.enviar),
    url('^bancodeprovas/', banco_provas.BancoView),

    #Busca em atas,páginas e notícias
    url(r'^busca/$', busca.BuscaView),

    #Busca em uma das três cartegorias
    url(r'^busca/(?P<tipo>(ata|pagina|noticia))/(?P<pag>[0-9]*)$', busca.BuscaCartegoriaView),

    #Ouvidoria
    url(r'^contato/', ouvidoria.view),

    #Banco de Livros
    url(r'^bancodelivros/', banco_livro.LivroView),

    #urls da interface de admin
    url(r'^admin/', admin.site.urls),
]



# if settings.DEBUG:
#     urlpatterns += patterns('',
#         url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#             'document_root': settings.MEDIA_ROOT,
#         }),
#         url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
#             'document_root': settings.STATIC_ROOT,
#         }),
#     )
