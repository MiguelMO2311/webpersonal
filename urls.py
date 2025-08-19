from django.contrib import admin
from django.urls import path
from django.conf import settings

from core import views as core_views
from portfolio import views as portfolio_views



urlpatterns = [
    path('', core_views.home, name="home"),
    path('about-me/', core_views.about, name="about"),
    path('portfolio/', portfolio_views.portfolio, name="portfolio"),
    path('contact/', core_views.contact, name="contact"),
    path('admin/', admin.site.urls),
    path("contact/send_email/", core_views.send_email, name="send_email"),
    path('admin-cv/', core_views.mi_vista_admin_cv, name='cv_admin'),
    path('fsd-cv/', core_views.mi_vista_fsd_cv, name='cv_fsd'),
    path('camino/', core_views.el_camino_recorrido, name='camino'),
    path('camino/about.html', core_views.about_camino, name='about_camino')

]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

