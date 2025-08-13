document.addEventListener('DOMContentLoaded', function () {
    // Floating label form group behavior
    document.body.addEventListener('input', function (e) {
        if (e.target.closest('.floating-label-form-group')) {
            const group = e.target.closest('.floating-label-form-group');
            group.classList.toggle(
                'floating-label-form-group-with-value',
                !!e.target.value
            );
        }
    });

    document.body.addEventListener('focus', function (e) {
        if (e.target.closest('.floating-label-form-group')) {
            e.target.closest('.floating-label-form-group').classList.add('floating-label-form-group-with-focus');
        }
    }, true);

    document.body.addEventListener('blur', function (e) {
        if (e.target.closest('.floating-label-form-group')) {
            e.target.closest('.floating-label-form-group').classList.remove('floating-label-form-group-with-focus');
        }
    }, true);

    // Navbar scroll behavior for screens wider than 992px
    const nav = document.getElementById('mainNav');
    if (window.innerWidth > 992 && nav) {
        let previousTop = 0;
        const navHeight = nav.offsetHeight;

        window.addEventListener('scroll', function () {
            const currentTop = window.scrollY;

            if (currentTop < previousTop) {
                // Scrolling up
                if (currentTop > 0 && nav.classList.contains('is-fixed')) {
                    nav.classList.add('is-visible');
                } else {
                    nav.classList.remove('is-visible', 'is-fixed');
                }
            } else {
                // Scrolling down
                nav.classList.remove('is-visible');
                if (currentTop > navHeight && !nav.classList.contains('is-fixed')) {
                    nav.classList.add('is-fixed');
                }
            }
            previousTop = currentTop;
        });
    }

    // Extra logic to prevent navbar class conflicts on small screens
    const navCollapse = document.getElementById('navbarResponsive');
    const toggler = document.querySelector('.navbar-toggler');

    const isMenuOpen = () => navCollapse && navCollapse.classList.contains('show');

    const cleanNavClasses = () => {
        if (window.innerWidth < 992 && isMenuOpen()) {
            nav.classList.remove('is-fixed', 'is-visible');
        }
    };

    if (toggler) {
        toggler.addEventListener('click', function () {
            setTimeout(cleanNavClasses, 300);
        });
    }

    window.addEventListener('scroll', cleanNavClasses);
});
