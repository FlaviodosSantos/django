from django.urls import path
from django.urls.resolvers import URLPattern
from .views import person_list


urlpatterns = [
    path('list/', person_list),
]