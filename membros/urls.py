from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^\/?$', views.InstitucionalView, name="HomeInstitucional"),
    url(r'^\/inscricao\/?$', views.forms_incricao_membros , name="membrosIncricao"),
]
