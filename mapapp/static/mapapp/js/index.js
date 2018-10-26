(() => {
    document.addEventListener('DOMContentLoaded', function () {
        // Initialize collapsible
        const $collapsible = document.querySelector('.collapsible');
        M.Collapsible.init($collapsible);

        // Initialize tooltips
        const $toolTips = document.querySelectorAll('.tooltipped');
        M.Tooltip.init($toolTips);

        const sideNav = document.querySelector('[data-js=side-panel]');
        const openSidenavBtn = document.querySelector('[data-js=open-sidenav]');
        const formSearch = document.querySelector('[data-js=form-search]');
        const input = document.querySelector('[data-js=search]');
        const resellerList = document.querySelector('[data-js=reseller-list]');
        const li = Array.from(resellerList.getElementsByTagName('li'));
        const flashCloseButton = document.querySelector('.flash-close');

        formSearch &&
            formSearch.addEventListener('submit', event => {
                event.preventDefault();
            });

        openSidenavBtn &&
            openSidenavBtn.addEventListener('click', event => {
                event.preventDefault();

                // Toggle opening and closing of sideNav
                sideNav.classList.toggle('side-panel--close');

                // Move zoom panel
                const zoomPanel = document.querySelector('div.leaflet-top.leaflet-left');
                zoomPanel.classList.toggle('zoom-panel--close')
            });

        // Filter search bar
        input &&
            input.addEventListener('keyup', event => {
                event.preventDefault();

                const inputValue = input.value.toLowerCase();

                li.forEach((element, index) => {
                    const text = element.getElementsByTagName('span')[0].innerText.toLowerCase();

                    if (text.indexOf(inputValue) > -1) {
                        element.style.display = "block";
                    }
                    else {
                        element.style.display = "none";
                    }
                });
            });

        // Click event on flash message
        flashCloseButton &&
            flashCloseButton.addEventListener("click", function () {
                const flashMessage = document.querySelector('.messages');
                flashMessage.parentNode.removeChild(flashMessage);
            });
    });
})();
