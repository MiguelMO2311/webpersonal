# trunk-ignore-all(isort)
import os
from django.shortcuts import render
from django.http import JsonResponse
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from portfolio.models import Project, Diploma
from decouple import config


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
    
def el_camino_recorrido(request):
    return render(request, 'core/el_camino_recorrido.html')

# Envío de correo con SendGrid
def send_email(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        mensaje = request.POST.get("mensaje")

        if not nombre or not email or not mensaje:
            return JsonResponse({"success": False, "error": "Todos los campos son obligatorios."}, status=400)

        asunto = f"Mensaje de {nombre}"
        cuerpo = f"De: {email}\n\n{mensaje}"

        email_obj = Mail(
            from_email=config('SENDGRID_FROM_EMAIL'),
            to_emails=config('SENDGRID_TO_EMAIL'),
            subject=asunto,
            plain_text_content=cuerpo
        )

        try:
            sg = SendGridAPIClient(config('SENDGRID_API_KEY'))
            response = sg.send(email_obj)
            if response.status_code == 202:
                return JsonResponse({"success": True, "message": "Correo enviado correctamente."})
            else:
                return JsonResponse({"success": False, "error": "Error al enviar el correo."}, status=500)
        except Exception as e:
            import traceback
            print(traceback.format_exc())
            return JsonResponse({"success": False, "error": "Error interno al enviar el correo."}, status=500)


    return JsonResponse({"success": False, "error": "Método no permitido."}, status=400)
