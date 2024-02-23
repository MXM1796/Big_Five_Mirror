# Importieren der erforderlichen Module und Funktionen

import numpy as np
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

#todo change name and location of semantic_search py file
import data_transfer.python_src.semantic_search as ses
from data_transfer.python_src.database_upload import upload_function

#  Schreibe Funktion um die Daten vom post request von content.js zu empfangen

@csrf_exempt
def receive_data(request):
    if request.method == 'POST':
        # Hier können Sie die Daten aus der Anfrage verarbeiten
        # WICHTIG: Daten werden im body übergeben!!!
        received_data = request.body

        # Daten in der Datenbank speichern
        upload_function(str(received_data))

        # Beispielantwort - wird bei "Data updated" in der Konsole abgebildet
        response_data = {'status': 'success', 'message': 'Daten erfolgreich empfangen',
                         "Empfamngene Daten": str(received_data)}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'status': 'error', 'message': 'Ungültige Anfrage-Methode'})



# Dekorieren der Funktion 'my_api_endpoint' als API-Ansicht, die nur GET-Anfragen akzeptiert
@api_view(['GET'])
def my_api_endpoint(request):
    # Behandeln der Anfrage und Vorbereiten einer Antwort
    response_data = {"message": ses.score_arr_full}
    return Response(response_data)


# Definition der Indexansichtsfunktion
def index(request):
    return render(request, 'index.html', {})
