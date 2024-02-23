// Importieren der Datei "py_to_js_transfer.js", falls benötigt
import "./py_to_js_transfer.js";

// Diese Funktion nimmt Daten entgegen und erstellt ein Polarchart.
export function plottingData(score_arr) {
  // Daten für das Streudiagramm
  var data = [{
    type: 'scatterpolar', // Diagrammtyp: polarisiertes Streudiagramm
    r: score_arr, // Radienwerte für die Datenpunkte
    theta: ['O', 'C', 'E', 'A', 'N'], // Winkelkoordinaten für die Datenpunkte
    fill: 'toself' // Füllen des Bereichs unter der Kurve
  }];

  // Layouteinstellungen für das Diagramm
  var layout = {
    polar: {
      radialaxis: {
        visible: true,
        range: [0, 1] // Wertebereich für die radialen Achsen
      }
    },
    showlegend: false // Legende im Diagramm ausblenden
  };

  // Erstellen und Anzeigen des Diagramms in einem HTML-Element mit der ID 'plot'
  Plotly.newPlot('plot', data, layout);

  // Konsolenausgabe der empfangenen Daten
  console.log(score_arr);
}
