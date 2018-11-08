document.addEventListener("DOMContentLoaded", () => {
  async function getResponse() {
    const res = await fetch("/reseller-data");
    const resellerData = await res.json();

    // List to hold markers
    const resellerMarkers = [];

    // Creating a new marker cluster group
    const clusterMarkers = L.markerClusterGroup();

    // Get resellers length
    const resellers = resellerData.resellers;

    resellers.forEach((element, index) => {
      // Get data fields
      const first_name = element.first_name,
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
      const resellerMarker = L.marker([latitude, longitude]).bindPopup(
        `<h6>${first_name} ${last_name}</h6><ul><li>${company}</li><li>${address}</li><li>${city}, ${state} ${zipcode}</li><li>em: ${email}</li><li>ph: ${phone}</li><li>Notes: ${comments}</li></ul></p>`
      );

      // Push markers to list
      resellerMarkers.push(resellerMarker);

      // Add layer to clusterMarkers
      clusterMarkers.addLayer(resellerMarker);
    });

    // Create marker layer
    const resellerLocations = L.layerGroup(resellerMarkers);

    // Send layers to createMap function
    const myMap = await createMap(resellerLocations, clusterMarkers);

    return myMap;
  }

  function createMap(orderLocations, clusterMarkers) {
    // Mapbox wordmark
    const mbAttr =
      'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
      '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
      'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>, ' +
      'Click <a href="/map">here</a> for full map.',
      mbKey =
        "pk.eyJ1IjoiamF5bGVoIiwiYSI6ImNqaDFhaWo3MzAxNTQycXFtYzVraGJzMmQifQ.JbX9GR_RiSKxSwz9ZK4buw",
      mbUrl = `https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=${mbKey}`,
      mbStyleUrl = `https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/256/{z}/{x}/{y}?access_token=${mbKey}`;

    // Define light layer
    const light = L.tileLayer(mbUrl, { id: "mapbox.light", attribution: mbAttr }),
      streets = L.tileLayer(mbStyleUrl, {
        id: "streets-v10",
        attribution: mbAttr
      }),
      dark = L.tileLayer(mbUrl, { id: "mapbox.dark", attribution: mbAttr }),
      naviNight = L.tileLayer(mbStyleUrl, {
        id: "navigation-preview-night-v2",
        attribution: mbAttr
      }),
      satellite = L.tileLayer(mbUrl, {
        id: "mapbox.satellite",
        attribution: mbAttr
      });

    // Define baseMaps object to hold our base layers
    const baseMaps = {
      Light: light,
      Streets: streets,
      Dark: dark,
      Night: naviNight,
      Satellite: satellite
    };

    // Create overlay object to hold overlay layer
    const overlayMaps = {
      "Cluster Groups": clusterMarkers,
      "All Order Locations": orderLocations
    };

    // Create map
    const myMap = L.map("map", {
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

    return myMap;
  }

  getResponse().then(myMap => {
    const addressSearch = document.querySelector(
      "[data-js=form-address-search]"
    );
    const addressInput = document.querySelector("[data-js=address-search]");

    function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== "") {
        let cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
          // let cookie = jQuery.trim(cookies[i]);
          let cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === name + "=") {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }

    addressSearch &&
      addressSearch.addEventListener("submit", async event => {
        event.preventDefault();

        const addressInputValue = addressInput.value.trim();

        if (addressInputValue !== "") {
          const res = await fetch("/address-location", {
            method: "POST",
            credentials: "same-origin",
            headers: {
              "X-CSRFToken": getCookie("csrftoken"),
              Accept: "application/json",
              "Content-Type": "application/json"
            },
            body: JSON.stringify({ address: addressInputValue })
          });

          const json = await res.json();
          const addressDetails = json.results;

          try {
            const lat = addressDetails.latlng[0];
            const lng = addressDetails.latlng[1];
            const formatted_address = addressDetails.formatted_address;

            myMap.setView(new L.LatLng(lat, lng), 10);

            let redMarker = L.icon({
              iconUrl: "/static/mapapp/img/red_marker.png",
              iconSize: [50, 48],
              iconAnchor: [25, 48],
              popupAnchor: [0, -38]
            });

            let searchMarker = new L.marker(addressDetails.latlng, {
              icon: redMarker
            }).bindPopup(`${formatted_address}`).addTo(myMap);

            searchMarker &&
              searchMarker.addEventListener("contextmenu", event => {
                myMap.removeLayer(searchMarker);
              });
          }
          catch (error) {
            // console.log(error);
            M.toast({html: `No results for ${addressInputValue}`});
          }
        }
      });
  });
});
