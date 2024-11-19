import imaplib
import email
from email.header import decode_header
import datetime

# Conectar a la cuenta de Gmail
username = "tu_correo@gmail.com"
password = "tu_contraseña"
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username, password)

# Seleccionar la bandeja de entrada
mail.select("inbox")

# Buscar correos por fecha
date = (datetime.date.today() - datetime.timedelta(1)).strftime("%d-%b-%Y")
result, data = mail.search(None, f'(SENTSINCE {date})')

# Buscar correos por asunto
# result, data = mail.search(None, '(SUBJECT "asunto")')

# Obtener los IDs de los correos
email_ids = data[0].split()

# Procesar cada correo
for email_id in email_ids:
    result, msg_data = mail.fetch(email_id, "(RFC822)")
    raw_email = msg_data[0][1]
    msg = email.message_from_bytes(raw_email)
    
    # Decodificar el asunto
    subject, encoding = decode_header(msg["Subject"])[0]
    if isinstance(subject, bytes):
        subject = subject.decode(encoding if encoding else "utf-8")
    
    # Imprimir el asunto del correo
    print("Asunto:", subject)

# Cerrar la conexión
mail.logout()