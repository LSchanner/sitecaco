from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^\/?(?P<id>[0-9]*)', views.ProdutosView, name='Loja'),
]
