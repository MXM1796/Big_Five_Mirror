
// Sende URL an den server, der über Python operiert wird
function send_to_py(youtube_url){
    // sende daten an django view
    var dataToSend = JSON.stringify(youtube_url)

    // Check if data exists in localStorage
    if (dataToSend) {

        // Define the URL of your backend endpoint
        var backendEndpoint = 'http://127.0.0.1:8000/receive-data/';

        console.log("I am here")
        fetch(backendEndpoint,
        {
                method: "POST", // *GET, POST, PUT, DELETE, etc.
                headers: {
                  "Content-Type": "application/json",
                },
                body: dataToSend, // body data type must match "Content-Type" header

            })
        .then(response => {
            //handle response
            return response.json();
        })
        .then(data => {
            console.log('Data updated:', data)
        })
        .catch(error => {
            //handle error
            console.log(error)
          });

}}

// Überwachungsfunktion: Zur Detektion der geschauten Videos auf Youtube. Jedes Mal, wenn ein Video angeschaut wird,
// wird die Url, über eine Funktion, an meinen Server geschickt.
let previousUrl = '';
const observer = new MutationObserver(function(mutations) {
  if (location.href !== previousUrl) {
      previousUrl = location.href;
      // send location to Server, which is handled by python
      send_to_py(location.href)
    }
});
const config = {subtree: true, childList: true};

observer.observe(document, config)