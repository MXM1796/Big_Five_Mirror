# Django-URL-Konfiguration

from django.urls import path
from . import views

# Definieren der URL-Muster
urlpatterns = [
    # Muster für die Standardseite (Indexseite)
    path("", views.index, name="index"),

    # Muster für die API-Endpunktansicht
    path('api/endpoint/', views.my_api_endpoint),
]
