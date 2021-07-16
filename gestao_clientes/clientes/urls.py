from django.urls import path
from django.urls.resolvers import URLPattern
from .views import person_list, tela_inicio


urlpatterns = [
    path('list/', person_list),
    path('', tela_inicio),
]