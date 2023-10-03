/**
 * Dieses Skript sendet eine GET-Anfrage an einen Django-API-Endpunkt und verarbeitet die Antwort.
 */

// Importieren der plottingData-Funktion aus der Datei 'display_graphs.js'
import { plottingData } from './display_graphs.js';

// Definieren der API-Endpunkt-URL
const apiEndpointUrl = 'http://localhost:8000/api/endpoint/';

// Senden einer GET-Anfrage an den Django-API-Endpunkt
fetch(apiEndpointUrl)
  .then(response => response.json()) // Wandelt die Antwort in JSON-Format um
  .then(data => {
      const currentUrl = window.location.href;
      console.log(currentUrl);

      // Verarbeiten der Antwort von Django

      // Extrahieren der Nachrichten aus den empfangenen Daten
      const messages = data.message;

      // Aufrufen der 'plottingData'-Funktion, um die empfangenen Nachrichten zu verarbeiten
      plottingData(messages);
  })
  .catch(error => {
      // Behandeln von Fehlern, die während der Anfrage auftreten können
      console.error('Fehler bei der Anfrage an die API:', error);
  });

