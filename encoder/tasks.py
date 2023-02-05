from time import sleep
from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage
from .models import EncodedDataDownload,DecodedDataDownload

@shared_task()
def send_mail_encode(user,file):
    subject = "Successful File Operation"
    message = "Your request has been processed.\n Please find the attached file, thank you for using Encoder&Decoder"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user]

    files = EncodedDataDownload.objects.filter(name=file).values()[0]['data']

    email_mess = EmailMessage(
    subject,
    message,
    email_from,
    recipient_list
    )

    email_mess.attach(f"{file}.txt",files,'application/*')
    email_mess.send()

@shared_task()
def send_mail_decode(user,file):
    subject = "Successful File Operation"
    message = "Your request has been processed.\nPlease find the attached file.\nThank you for using Encoder&Decoder"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user]

    files = DecodedDataDownload.objects.filter(name=file).values()[0]['data']

    email_mess = EmailMessage(
    subject,
    message,
    email_from,
    recipient_list
    )

    email_mess.attach(file[:-4],files,'application/*')
    email_mess.send()
