import os
from django.core.mail import send_mail
from django.template.loader import render_to_string
from main.models import User
from simple_cms.celery import app
from simple_cms.settings import BASE_DIR, EMAIL_HOST_USER


@app.task
def send_email(email, text):
    html_message = render_to_string(
        os.path.join(BASE_DIR, 'templates/email.html'),
        {'text': text}
    )

    send_mail(
        'Что же Вы написали?',
        html_message,
        EMAIL_HOST_USER,
        [email],
        html_message=html_message
    )
