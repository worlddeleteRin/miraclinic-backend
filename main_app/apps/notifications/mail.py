from config import settings
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from fastapi.background import BackgroundTasks

conf = ConnectionConfig(
    MAIL_USERNAME = settings.mail_username,
    MAIL_PASSWORD = settings.mail_password,
    MAIL_FROM = settings.mail_from,
    MAIL_PORT = settings.mail_port,
    MAIL_SERVER = settings.mail_server,
    # MAIL_TLS = True,
    MAIL_SSL = True,
    USE_CREDENTIALS = True,
    TEMPLATE_FOLDER = 'apps/notifications/templates/email'
)

def send_mail_background(
    background_tasks: BackgroundTasks,
    subject: str,
    email_to: str,
    body: dict,
):
    message = MessageSchema(
        subject = subject,
        recipients = [email_to],
        template_body = body,
        subtype = 'html',
    )
    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message, template_name='request_call.html')
