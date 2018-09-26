from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'main-crismando/', views.main_crismando, name='main_crismando'),
    url(r'novo-crismando/', views.novo_crismando, name='novo_crismando'),
    url(r'filtrar-crismando/', views.filtrar_crismando, name='filtrar_crismando'),
]
