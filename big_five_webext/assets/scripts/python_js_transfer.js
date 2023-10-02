import { plottingData } from './display_graphs.js';

// Sending a GET request to the Django API endpoint
fetch('http://localhost:8000/api/endpoint/')
  .then(response => response.json())
  .then(data => {
      console.log(data)
      // Handle the response from Django
      // var messages = data.message
      // plottingData(messages)

  })


