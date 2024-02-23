# Django-URL-Konfiguration
from django.template.defaulttags import url
from django.urls import path
from . import views

# Definieren der URL-Muster
urlpatterns = [
    # Standardseite (Indexseite)
    path("", views.index, name="index"),

    # API-Endpunktansicht
    path('api/endpoint/', views.my_api_endpoint,  name='my_api_endpoint'),

    # API - Datenempfang von content js
    path('receive-data/', views.receive_data, name='receive_data'),
]
