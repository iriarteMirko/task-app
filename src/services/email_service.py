import smtplib
from jinja2 import Environment, FileSystemLoader
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
from src.config import AppConfig
import os


class GmailSender:
    def __init__(self, sender_email: str, password: str):
        self.sender_email = sender_email
        self.password = password
        self.smtp_server = 'smtp.gmail.com'
        self.smtp_port = 587
        self.env = Environment(loader=FileSystemLoader('src/templates'))
    
    def send_email(self, recipient_emails: list, subject: str, body: dict, cc_emails: list = None, files: list = None):
        """ Envía un correo electrónico a los destinatarios especificados. """
        
        msg = MIMEMultipart() # Mensaje
        
        msg['From'] = self.sender_email # Remitente
        msg['To'] = ', '.join(recipient_emails) # Destinatarios
        msg['Subject'] = subject # Asunto
        
        # Destinararios en copia
        if cc_emails:
            msg['CC'] = ', '.join(cc_emails)
        
        # Cuerpo del correo
        template = self.env.get_template('email_body.html')
        body_html = template.render(body)
        
        msg_alternative = MIMEMultipart('alternative')
        msg.attach(msg_alternative)
        
        msg_text = MIMEText(body_html, 'html')
        msg_alternative.attach(msg_text)
        
        # Firma
        try:
            with open(AppConfig.ICONS["firma"], 'rb') as img:
                msg_image = MIMEImage(img.read())
                msg_image.add_header('Content-ID', '<signature_image>')
                msg.attach(msg_image)
        except Exception as e:
            print(f'Error adjuntando la imagen de firma: {str(e)}')
        
        # Archivos adjuntos
        if files:
            for file in files:
                try:
                    with open(file, 'rb') as attachment:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file)}')
                    msg.attach(part)
                except Exception as e:
                    print(f'Error adjuntando el archivo {file}: {str(e)}')
        
        # Enviar correo
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.password)
            all_recipients = recipient_emails + (cc_emails if cc_emails else [])
            server.sendmail(self.sender_email, all_recipients, msg.as_string())
            print('Correo enviado exitosamente.')
        except Exception as e:
            print(f'Error al enviar el correo: {str(e)}')
        finally:
            server.quit()