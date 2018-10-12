document.addEventListener('DOMContentLoaded', function () {
    let $sidenav = document.querySelector('.sidenav'),
        options = {
            closeOnClick: false
        }
    // M.Sidenav.init($sidenav, options);

    let instance = M.Sidenav.getInstance($sidenav);

    console.log(instance);

    // Sidenav open and close buttons
    let openSidenavBtn = document.querySelector('.open-sidenav'),
        closeSidenavBtn = document.querySelector('.close-sidenav');

    openSidenavBtn.addEventListener('click', function () {
        instance.open();
    });

    closeSidenavBtn.addEventListener('click', function () {
        instance.close();
    });
});