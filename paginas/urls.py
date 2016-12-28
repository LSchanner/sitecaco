from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.HomeView),
    url(r'^eventos\/?$', views.EventosView),
    url(r'^servicos\/?$', views.ServicosView),

    # This is the url for flatpages
    url(r'', include('django.contrib.flatpages.urls')),
]
