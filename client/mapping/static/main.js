// Initialize the platform object with your API key
var platform = new H.service.Platform({
    'apikey': 'OFWRe_xJYEKIPUgaNJWKAOepMzpqVudUuoOQZ25m2_M'
});

// Obtain the default map types from the platform object
var defaultLayers = platform.createDefaultLayers();

// Instantiate (and display) a map object:
var map = new H.Map(
    document.getElementById('map'),
    defaultLayers.vector.normal.map,
    {
        zoom: 10,
        center: { lat: 52.5, lng: 13.4 } // Default center coordinates
    }
);

// Enable the event system on the map instance:
var mapEvents = new H.mapevents.MapEvents(map);

// Instantiate the default behavior, providing the mapEvents object:
var behavior = new H.mapevents.Behavior(mapEvents);

// Create the default UI:
var ui = H.ui.UI.createDefault(map, defaultLayers);

// Function to add markers to the map
// Function to add markers to the map
function addMarkers(data) {
    // Static data with latitude, longitude, and title for each marker
    var staticData = [
        { lat: 52.520008, lng: 13.404954, title: 'Berlin, Germany' },
        { lat: 48.8566, lng: 2.3522, title: 'Paris, France' },
        { lat: 51.5074, lng: -0.1278, title: 'London, UK' }
        // Add more static data as needed
    ];

    staticData.forEach(function (item) {
        var marker = new H.map.Marker(item);
        map.addObject(marker);
    });
}

// Call the addMarkers function to display the markers
addMarkers();


fetch('/get_items', {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    },
})
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log(data); // Check data structure in console
        addMarkers(data);
    })
    .catch(error => console.error('Error fetching location data:', error.message, error.response));




// Search functionality
var searchService = platform.getSearchService();

document.getElementById('search-button').addEventListener('click', function () {
    var query = document.getElementById('search-input').value;

    searchService.geocode({
        q: query
    }, (result) => {
        // Clear previous markers
        map.getObjects().forEach(function (obj) {
            if (obj instanceof H.map.Marker) {
                map.removeObject(obj);
            }
        });

        // Add markers for search results
        result.items.forEach(function (item) {
            var marker = new H.map.Marker(item.position);
            map.addObject(marker);
            map.setCenter(item.position);
        });
    }, (error) => {
        console.error('Geocode error:', error);
    });
});
