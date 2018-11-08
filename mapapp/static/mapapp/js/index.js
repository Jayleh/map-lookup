document.addEventListener("DOMContentLoaded", () => {
  // Enable floating action button
  let $actionBtn = document.querySelectorAll('.fixed-action-btn');
  M.FloatingActionButton.init($actionBtn);

  // Initialize collapsible
  const $collapsible = document.querySelector(".collapsible");
  M.Collapsible.init($collapsible);

  // Initialize tooltips
  const $toolTips = document.querySelectorAll(".tooltipped");
  M.Tooltip.init($toolTips);

  const sideNav = document.querySelector("[data-js=side-panel]");
  const openSidenavBtn = document.querySelector("[data-js=open-sidenav]");
  const filterSearch = document.querySelector("[data-js=form-filter-search]");
  const filterInput = document.querySelector("[data-js=filter-search]");
  const resellerList = document.querySelector("[data-js=reseller-list]");
  const li = Array.from(resellerList.getElementsByTagName("li"));
  const flashCloseButton = document.querySelector(".flash-close");

  filterSearch &&
    filterSearch.addEventListener("submit", event => {
      event.preventDefault();
    });

  openSidenavBtn &&
    openSidenavBtn.addEventListener("click", event => {
      event.preventDefault();

      // Toggle opening and closing of sideNav
      sideNav.classList.toggle("side-panel--close");

      // Move zoom panel
      const zoomPanel = document.querySelector("div.leaflet-top.leaflet-left");
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
    flashCloseButton.addEventListener("click", function () {
      const flashMessage = document.querySelector(".messages");
      flashMessage.parentNode.removeChild(flashMessage);
    });
});
