(() => {
    document.addEventListener('DOMContentLoaded', function () {
        // Initialize collapsible
        const $collapsible = document.querySelector('.collapsible');
        M.Collapsible.init($collapsible);

        // Initialize tooltips
        const $toolTips = document.querySelectorAll('.tooltipped');
        M.Tooltip.init($toolTips);

        // Initialize scrollspy
        const $scrollspy = document.querySelector('.scrollspy');
        M.ScrollSpy.init($scrollspy);

        const sideNav = document.querySelector('[data-js=side-panel]');
        const openSidenavBtn = document.querySelector('[data-js=open-sidenav]');
        const formSearch = document.querySelector('[data-js=form-search]')

        formSearch &&
            formSearch.addEventListener("submit", event => {
                event.preventDefault();
            });

        openSidenavBtn &&
            openSidenavBtn.addEventListener('click', event => {
                event.preventDefault();

                // Toggle opening and closing of sideNav
                sideNav.classList.toggle("side-panel--close");
            });
    });
})();

