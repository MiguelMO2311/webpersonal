from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
import ssl
import certifi
from django.http import JsonResponse
import os



# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")

os.environ["SSL_CERT_FILE"] = certifi.where()
ssl_context = ssl.create_default_context()
ssl_context.load_verify_locations(certifi.where())

# Desactivar la verificación de certificados SSL (Solo para pruebas)
ssl._create_default_https_context = ssl._create_unverified_context


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
