// let sidenav = document.getElementById('sidenav');
// let sidneavMobile = document.getElementById('sidenav-mobile');
const IS_NAV_EXPAND_KEY = "isNavBarExpand";

if ($('sidenav').hasClass('-active')) {
    $('sidebar-block').css({
        "min-width": "200px"
    });
} else {
    $('sidebar-block').css({
        "min-width": "80px"
    });
}

$('#header-menu').on('click', function () {
    if ($('body').width() <= 805) {
        //if mobile

        $('#sidenav').toggleClass('-active');
        $('#sidenav-mobile').toggleClass('-collapsed');
        $('#overlay-wrap').toggleClass('-apply-overlay');
        $('#header-menu-mobile').toggleClass('-active');


        if ($('#sidenav-mobile').hasClass('-collapsed')) {
            //if sidenav is active

            $('#overlay-wrap').on('click', function () {

                $('#sidenav').removeClass('-active');
                $('#sidenav-mobile').removeClass('-collapsed');
                $('#overlay-wrap').removeClass('-apply-overlay');
                $('#header-menu-mobile').removeClass('-active');

            });

            $('#header-menu-mobile').on('click', function () {

                $('#sidenav').removeClass('-active');
                $('#sidenav-mobile').removeClass('-collapsed');
                $('#overlay-wrap').removeClass('-apply-overlay');
                $('#header-menu-mobile').removeClass('-active');

            });

        } else {
            //if sidenav is not active

            $('#sidenav').addClass('-active');
            $('#sidenav-mobile').addClass('-collapsed');
            $('#content-block').addClass('-apply-overlay');


        }


    } else {
        //if desktop
        $('#sidenav').toggleClass('-active');
        $('#sidenav-mobile').toggleClass('-collapsed');
        $('#content-block').toggleClass('-extend');
    }
});


$(window).on('resize', function () {

    if ($('sidenav').hasClass('-active')) {
        $('sidebar-block').css({
            "min-width": "200px"
        });
    } else {
        $('sidebar-block').css({
            "min-width": "80px"
        });
    }


    if ($('body').width() <= 805) {
        //if mobile

        if ($('#sidenav').hasClass('-active')) {
            //if sidenav has class active
            $('#overlay-wrap').addClass('-apply-overlay');
            $('#header-menu-mobile').addClass('-active');

            $('#overlay-wrap').on('click', function () {

                $('#sidenav').removeClass('-active');
                $('#sidenav-mobile').removeClass('-collapsed');
                $('#overlay-wrap').removeClass('-apply-overlay');
                $('#header-menu-mobile').removeClass('-active');

            });

            $('#header-menu-mobile').on('click', function () {

                $('#sidenav').removeClass('-active');
                $('#sidenav-mobile').removeClass('-collapsed');
                $('#overlay-wrap').removeClass('-apply-overlay');
                $('#header-menu-mobile').removeClass('-active');

            });

        } else {
            //if sidenav did not have class active

        }

    } else {
        //if desktop

        $('#overlay-wrap').removeClass('-apply-overlay');
        $('#header-menu-mobile').removeClass('-active');

    }
});


function activeNavIcon(desktopNavLocator, mobileLocator) {
    $(desktopNavLocator).toggleClass('-active');
    $(mobileLocator).toggleClass('-active-mobile');
}

// navigation expansion onlick
$("#header-menu").click(function () {
    let isNavBarExpand = sessionStorage.getItem(IS_NAV_EXPAND_KEY);
    if (isNavBarExpand != null) {
        if (isNavBarExpand == 1) {
            sessionStorage.setItem(IS_NAV_EXPAND_KEY, 0);
        } else {
            sessionStorage.setItem(IS_NAV_EXPAND_KEY, 1);
        }
    } else {
        sessionStorage.setItem(IS_NAV_EXPAND_KEY, 1);
    }
});

$(document).ready(function () {
    let isNavBarExpand = sessionStorage.getItem(IS_NAV_EXPAND_KEY);
    if (isNavBarExpand != null) {
        if (isNavBarExpand == 1) {
            //todo
            //expand nav bar
        } else {
            //todo
            //close nav bar
        }
    } else {
        sessionStorage.setItem(IS_NAV_EXPAND_KEY, 0);
    }
});









