from django.conf import settings
from django.core.mail import send_mail

def sendmessage(To,msg):
    subject = "Encoder and Decoder"
    message = "Hello Good Morning"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [To]
    try:
        send_mail(subject,message,email_from,recipient_list)
    except e:
        print(e.message)
