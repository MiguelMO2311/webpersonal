from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

email_obj = Mail(
    from_email='mmeneses73@gmail.com',
    to_emails='mmeneses73@gmail.com',
    subject='Prueba desde script',
    plain_text_content='Este es un correo de prueba.'
)

try:
    sg = SendGridAPIClient('SG.tu_clave_aquí')  # ← pega la clave directamente aquí
    response = sg.send(email_obj)
    print("Código de respuesta:", response.status_code)
except Exception as e:
    print("ERROR:", e)
