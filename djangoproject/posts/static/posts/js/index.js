document.addEventListener('DOMContentLoaded', function () {
    // Initialize collapsible
    let $collapsible = document.querySelector('.collapsible');
    M.Collapsible.init($collapsible);

    // Side panel
    let sideNav = document.querySelector('.side-panel');

    // Side panel open and close buttons
    let openSidenavBtn = document.querySelector('.open-sidenav');

    openSidenavBtn.addEventListener('click', function () {
        let sideNavClassList = sideNav.classList;

        if (sideNavClassList.contains('close')) {
            sideNav.style.transform = "translateX(0%)";
            sideNavClassList.remove('close');
            sideNavClassList.add('open');
        }
        else if (sideNavClassList.contains('open')) {
            sideNav.style.transform = "translateX(-105%)";
            sideNavClassList.remove('open');
            sideNavClassList.add('close');
        }
    });
});