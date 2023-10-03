# Importieren der erforderlichen Module und Funktionen
import numpy as np
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pyth_data_transfer.python_src.semantic_search as ses

# Dekorieren der Funktion 'my_api_endpoint' als API-Ansicht, die nur GET-Anfragen akzeptiert
@api_view(['GET'])
def my_api_endpoint(request):
    # Behandeln der Anfrage und Vorbereiten einer Antwort
    response_data = {"message": ses.score_arr_full}
    return Response(response_data)

# Definition der Indexansichtsfunktion
def index(request):
    return render(request, 'index.html', {})
