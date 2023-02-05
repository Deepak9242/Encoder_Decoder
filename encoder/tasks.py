from time import sleep
from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage
from .models import EncodedDataDownload,DecodedDataDownload

@shared_task()
def send_mail(user,file,typ):
    subject = "Successful File Operation"
    message = f"Your request has been processed. Please find the attached file, thank you for using Encoder&Decoder"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user]
    if typ=="encode":
        files = EncodedDataDownload.objects.filter(name=file).values()[0]['data']
        file = file + ".txt"
    else:
        files = DecodedDataDownload.objects.filter(name=file).values()[0]['data']

    email_mess = EmailMessage(
    subject,
    message,
    email_from,
    recipient_list
    )

    email_mess.attach(file,files,'application/*')
    email_mess.send()
