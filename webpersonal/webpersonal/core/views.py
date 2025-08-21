import os
import ssl
import certifi

from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from portfolio.models import Project, Diploma


# Vistas estándar
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")

def mi_vista_admin_cv(request):
    return render(request, 'core/cv_admin.html')

def mi_vista_fsd_cv(request):
    return render(request, 'core/cv_fsd.html')

# Vista para el portfolio con proyectos y diplomas
def portfolio(request):
    projects = Project.objects.all()
    diplomas = Diploma.objects.all()
    return render(request, "core/portfolio.html", {
        "projects": projects,
        "diplomas": diplomas,
    })

# Configuración SSL (desactivación temporal para pruebas)
os.environ["SSL_CERT_FILE"] = certifi.where()
ssl_context = ssl.create_default_context()
ssl_context.load_verify_locations(certifi.where())
ssl._create_default_https_context = ssl._create_unverified_context

# Envío de correo
def send_email(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        mensaje = request.POST.get("mensaje")

        asunto = f"Mensaje de {nombre}"
        cuerpo = f"De: {email}\n\n{mensaje}"

        try:
            send_mail(
                asunto,
                cuerpo,
                settings.EMAIL_HOST_USER,
                ["mmeneses73@gmail.com"],
                fail_silently=False,
            )
            return JsonResponse({"success": True, "message": "Correo enviado correctamente."})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)

    return JsonResponse({"success": False, "error": "Método no permitido."}, status=400)
