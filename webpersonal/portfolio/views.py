from django.http import JsonResponse
from django.shortcuts import render
from .models import Project, Diploma  # ✅ Importamos también Diploma
from django.core.mail import send_mail
from django.conf import settings

# Vista del portfolio: carga proyectos y diplomas
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

        try:
            send_mail(
                subject=f"Mensaje de {nombre}",
                message=mensaje,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=["mmeneses73@gmail.com"],
                fail_silently=False,
                connection=settings.EMAIL_SSL_CONTEXT
            )
            return JsonResponse({"message": "Correo enviado correctamente"})
        except Exception as e:
            return JsonResponse({"error": f"Error al enviar el correo: {str(e)}"}, status=500)
    
    return JsonResponse({"error": "Método no permitido"}, status=405)
