from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
import ssl
import certifi

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")


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
                fail_silently=False,  # No hace falta definir conexión aquí
            )
            return redirect("contact")
        except Exception as e:
            return render(request, "core/contact.html", {"error": f"Error al enviar el correo: {str(e)}"})

    return render(request, "core/contact.html")
