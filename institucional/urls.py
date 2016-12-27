from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.InstitucionalView, name="HomeInstitucional"),
    url(r'^atas/(?P<pag>[0-9]*)', views.AtasView, name="ViewAtas"),
    url(r'^ata/(?P<id>[0-9]*)', views.AtaView, name="Ata"),
]
