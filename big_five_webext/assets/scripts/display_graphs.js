import "./python_js_transfer.js"

export function plottingData(data1) {
    var data = [{
      type: 'scatterpolar',
      r: data1,
      theta: ['O','C','E', 'A', 'N'],
      fill: 'toself'
    }]

    var layout = {
      polar: {
        radialaxis: {
          visible: true,
          range: [0, 50]
        }
      },
      showlegend: false
    }


  Plotly.newPlot('plot', data, layout);
    console.log(data1);
}