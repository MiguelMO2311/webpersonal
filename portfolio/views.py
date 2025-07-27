from django.http import JsonResponse
from django.shortcuts import render
from .models import Project, Diploma
from django.core.mail import send_mail
from django.conf import settings
import traceback
import ssl
import certifi
from django.core.mail import get_connection




# Vista del portfolio
def portfolio(request):
    projects = Project.objects.all()
    diplomas = Diploma.objects.all()
    return render(request, "portfolio/portfolio.html", {
        'projects': projects,
        'diplomas': diplomas,
    })

# Vista para enviar correos desde el formulario de contacto


def send_email(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        mensaje = request.POST.get("mensaje")

        if not nombre or not email or not mensaje:
            return JsonResponse({"success": False, "error": "Todos los campos son obligatorios."}, status=400)

        asunto = f"Mensaje de {nombre}"
        cuerpo = f"De: {nombre} <{email}>\n\n{mensaje}"

        try:
            ssl_context = ssl.create_default_context(cafile=certifi.where())
            connection = get_connection(
                ssl_context=ssl_context,
                fail_silently=False,
            )
            connection.open()

            send_mail(
                subject=asunto,
                message=cuerpo,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=["mmeneses73@gmail.com"],
                fail_silently=False,
                connection=connection
            )

            connection.close()

            return JsonResponse({"success": True, "message": "Correo enviado correctamente"})
        except Exception as e:
            traceback.print_exc()
            return JsonResponse({"success": False, "error": str(e)}, status=500)

    return JsonResponse({"success": False, "error": "Método no permitido"}, status=405)
