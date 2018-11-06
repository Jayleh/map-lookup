(() => {
  document.addEventListener("DOMContentLoaded", function() {
    // Initialize collapsible
    const $collapsible = document.querySelector(".collapsible");
    M.Collapsible.init($collapsible);

    // Initialize tooltips
    const $toolTips = document.querySelectorAll(".tooltipped");
    M.Tooltip.init($toolTips);

    const sideNav = document.querySelector("[data-js=side-panel]");
    const openSidenavBtn = document.querySelector("[data-js=open-sidenav]");
    const filterSearch = document.querySelector("[data-js=form-filter-search]");
    const addressSearch = document.querySelector(
      "[data-js=form-address-search]"
    );
    const filterInput = document.querySelector("[data-js=filter-search]");
    const addressInput = document.querySelector("[data-js=address-search]");
    const resellerList = document.querySelector("[data-js=reseller-list]");
    const li = Array.from(resellerList.getElementsByTagName("li"));
    const flashCloseButton = document.querySelector(".flash-close");

    filterSearch &&
      filterSearch.addEventListener("submit", event => {
        event.preventDefault();
      });

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

        console.log(addressInput.value);
        const res = await fetch("http://localhost:8000/address-location", {
          method: "POST",
          credentials: "same-origin",
          headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Accept": "application/json",
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ "address": addressInput.value })
        });

        const json = await res.json();

        // const address = json.latlng;

        console.log(json);
      });

    openSidenavBtn &&
      openSidenavBtn.addEventListener("click", event => {
        event.preventDefault();

        // Toggle opening and closing of sideNav
        sideNav.classList.toggle("side-panel--close");

        // Move zoom panel
        const zoomPanel = document.querySelector(
          "div.leaflet-top.leaflet-left"
        );
        zoomPanel.classList.toggle("zoom-panel--close");
      });

    // Filter search bar
    filterInput &&
      filterInput.addEventListener("keyup", event => {
        event.preventDefault();

        const inputValue = filterInput.value.toLowerCase();

        li.forEach((element, index) => {
          const text = element
            .getElementsByTagName("span")[0]
            .innerText.toLowerCase();

          if (text.indexOf(inputValue) > -1) {
            element.style.display = "block";
          } else {
            element.style.display = "none";
          }
        });
      });

    // Click event on flash message
    flashCloseButton &&
      flashCloseButton.addEventListener("click", function() {
        const flashMessage = document.querySelector(".messages");
        flashMessage.parentNode.removeChild(flashMessage);
      });
  });
})();
