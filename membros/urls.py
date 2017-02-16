from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^\/?$',
        views.homeMembros,
        name="homeMembros"
    ),
    # View para inscricao
    url(
        r'^\/inscricao\/?$',
        views.forms_incricao_membros ,
        name="membrosIncricao"
    ),
    # View para confirmacao de membro
    url(
        r'^\/confirmacao/(?P<token>[\w\s\-]+)\/?',
        views.dealToken,
        name='membrosDealToken'
    ),
]
