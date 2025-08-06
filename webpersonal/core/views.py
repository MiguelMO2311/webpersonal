import os
import ssl
import certifi

from django.http import JsonResponse
from django.shortcuts import render, redirect
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

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

# Envío de correo con SendGrid
def send_email(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        mensaje = request.POST.get("mensaje")

        asunto = f"Mensaje de {nombre}"
        cuerpo = f"De: {email}\n\n{mensaje}"

        email_obj = Mail(
            from_email='mmeneses73@gmail.com',  # Verificado en SendGrid
            to_emails='mmeneses73@gmail.com',
            subject=asunto,
            plain_text_content=cuerpo
        )

        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(email_obj)
            if response.status_code == 202:
                return JsonResponse({"success": True, "message": "Correo enviado correctamente."})
            else:
                return JsonResponse({"success": False, "error": "Error al enviar el correo."}, status=500)
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)

    return JsonResponse({"success": False, "error": "Método no permitido."}, status=400)
