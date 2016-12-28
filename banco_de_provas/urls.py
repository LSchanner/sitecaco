from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^\/?$', views.BancoView, name='homeBProva'),
    url(r'^\/enviar$', views.enviar, name='envioBProva')
]
