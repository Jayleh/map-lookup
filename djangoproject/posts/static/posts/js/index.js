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

        formSearch &&
            formSearch.addEventListener('submit', event => {
                event.preventDefault();
            });

        openSidenavBtn &&
            openSidenavBtn.addEventListener('click', event => {
                event.preventDefault();

                // Toggle opening and closing of sideNav
                sideNav.classList.toggle('side-panel--close');
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
    });
})();
