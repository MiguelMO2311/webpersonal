from django.contrib import admin
from django.urls import path
from core import views as core_views
from portfolio import views as portfolio_views
from core.views import home, send_email

from django.conf import settings

urlpatterns = [
    path('', core_views.home, name="home"),
    path('about-me/', core_views.about, name="about"),
    path('portfolio/', portfolio_views.portfolio, name="portfolio"),
    path('contact/', core_views.contact, name="contact"),
    path('admin/', admin.site.urls),
    path("", home, name="home"), 
    path("contact/send_email/", send_email, name="send_email"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

