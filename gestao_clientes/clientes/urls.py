from django.urls import path
from django.urls.resolvers import URLPattern
from .views import person_list, person_new


urlpatterns = [
    path('list/', person_list, name='person_list'),
    path('new/', person_new, name='person_new'),    
]