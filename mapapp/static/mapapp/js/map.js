function generateMap() {
    d3.json(`/reseller-data`, (error, resellerData) => {
        if (error) throw error;

        // console.log(resellerData);

        // List to hold markers
        let resellerMarkers = [];

        // Creating a new marker cluster group
        let clusterMarkers = L.markerClusterGroup();

        // Get resellers length
        let resellers = resellerData.resellers;

        resellers.forEach((element, index) => {
            // Get data fields
            let first_name = element.first_name,
                last_name = element.last_name,
                email = element.email,
                phone = element.phone,
                company = element.company,
                address = element.address,
                city = element.city,
                state = element.state,
                zipcode = element.zipcode,
                comments = element.comments,
                latitude = element.latitude,
                longitude = element.longitude;

            // Create marker and bind a pop-up
            let resellerMarker = L.marker([latitude, longitude])
                .bindPopup(
                    `<h6>${first_name} ${last_name}</h6><ul><li>${company}</li><li>${address}</li><li>${city}, ${state} ${zipcode}</li><li>em: ${email}</li><li>ph: ${phone}</li><li>Notes: ${comments}</li></ul></p>`
                );

            // Push markers to list
            resellerMarkers.push(resellerMarker);

            // Add layer to clusterMarkers
            clusterMarkers.addLayer(resellerMarker);
        });

        // console.log(resellerMarkers);

        // Create marker layer
        let resellerLocations = L.layerGroup(resellerMarkers);

        // console.log(resellerLocations);

        // Send earthquakes layer to createMap function
        createMap(resellerLocations, clusterMarkers);
    });
}

function createMap(orderLocations, clusterMarkers) {
    // Mapbox wordmark
    let mbAttr = 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
        '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>, ' +
        'Click <a href="/map">here</a> for full map.',
        mbKey = 'pk.eyJ1IjoiamF5bGVoIiwiYSI6ImNqaDFhaWo3MzAxNTQycXFtYzVraGJzMmQifQ.JbX9GR_RiSKxSwz9ZK4buw',
        mbUrl = `https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=${mbKey}`,
        mbStyleUrl = `https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/256/{z}/{x}/{y}?access_token=${mbKey}`;

    // Define light layer
    let light = L.tileLayer(mbUrl, { id: 'mapbox.light', attribution: mbAttr }),
        streets = L.tileLayer(mbStyleUrl, { id: 'streets-v10', attribution: mbAttr }),
        dark = L.tileLayer(mbUrl, { id: 'mapbox.dark', attribution: mbAttr }),
        naviNight = L.tileLayer(mbStyleUrl, { id: 'navigation-preview-night-v2', attribution: mbAttr }),
        satellite = L.tileLayer(mbUrl, { id: 'mapbox.satellite', attribution: mbAttr });

    // Define baseMaps object to hold our base layers
    let baseMaps = {
        Light: light,
        Streets: streets,
        Dark: dark,
        Night: naviNight,
        Satellite: satellite
    };

    // Create overlay object to hold overlay layer
    let overlayMaps = {
        'Cluster Groups': clusterMarkers,
        'All Order Locations': orderLocations
    };

    // Create map
    let myMap = L.map("map", {
        center: [39.4389, -98.6948],
        zoom: 4,
        layers: [streets, clusterMarkers]
    });

    // Create layer control
    L.control
        .layers(baseMaps, overlayMaps, {
            collapsed: true
        })
        .addTo(myMap);
}

// Run generateMap on initial load
generateMap();
