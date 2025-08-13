!function (i) {
    "use strict";

    // Floating label form group behavior
    i("body")
        .on("input propertychange", ".floating-label-form-group", function (o) {
            i(this).toggleClass("floating-label-form-group-with-value", !!i(o.target).val());
        })
        .on("focus", ".floating-label-form-group", function () {
            i(this).addClass("floating-label-form-group-with-focus");
        })
        .on("blur", ".floating-label-form-group", function () {
            i(this).removeClass("floating-label-form-group-with-focus");
        });

    // Navbar scroll behavior for screens wider than 992px
    if (i(window).width() > 992) {
        var o = i("#mainNav").height();
        i(window).on("scroll", { previousTop: 0 }, function () {
            var s = i(window).scrollTop();
            if (s < this.previousTop) {
                if (s > 0 && i("#mainNav").hasClass("is-fixed")) {
                    i("#mainNav").addClass("is-visible");
                } else {
                    i("#mainNav").removeClass("is-visible is-fixed");
                }
            } else {
                i("#mainNav").removeClass("is-visible");
                if (s > o && !i("#mainNav").hasClass("is-fixed")) {
                    i("#mainNav").addClass("is-fixed");
                }
            }
            this.previousTop = s;
        });
    }

}(jQuery);

// 🛠️ Extra logic to prevent navbar class conflicts on small screens
document.addEventListener('DOMContentLoaded', function () {
    const nav = document.getElementById('mainNav');
    const navCollapse = document.getElementById('navbarResponsive');

    const isMenuOpen = () => navCollapse && navCollapse.classList.contains('show');

    const cleanNavClasses = () => {
        if (window.innerWidth < 992 && isMenuOpen()) {
            nav.classList.remove('is-fixed', 'is-visible');
        }
    };

    const toggler = document.querySelector('.navbar-toggler');
    if (toggler) {
        toggler.addEventListener('click', function () {
            setTimeout(cleanNavClasses, 300);
        });
    }

    window.addEventListener('scroll', cleanNavClasses);
});
