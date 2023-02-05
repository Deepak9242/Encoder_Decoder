from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from encoder.forms import ImageForm
from encoder.encode import Encode_64,Decode_64
from encoder.messenger import sendmessage
from encoder.models import upload_encode,download_encode,upload_decode,download_decode
from encoder.tasks import send_mail_encode,send_mail_decode

# Create your views here.


def error(request):
    return render(request,"error.html")


def email(request):
    if request.method=="POST":
        #template = loader.get_template('uploaded.html')
        file_name = request.POST['filename']
        email = request.POST['email']
        typ = request.POST['typ']
        if typ=="encode":
            send_mail_encode.delay(email,file_name)
        else:
            send_mail_decode.delay(email,file_name)
        return render(request,"uploaded.html")
    else:
        return render(request,"error.html")

def decode(request):
    if request.method=='POST':
        if request.FILES['file'].size > 5*1024*1024:
            return HttpResponse("File Size TOO BIG")
        if request.FILES['file'] == None:
            return HttpResponse("No File Found")
        else:
            return handle_decode(request.FILES['file'])
    else:
        return render(request,"error.html")


def upload(request):
    #template = loader.get_template('uploaded.html')
    if request.method=='POST':
        if request.FILES['file'].size > 5*1024*1024:
            return HttpResponse("File Size TOO BIG")
        image = ImageForm(request.POST,request.FILES)
        if request.FILES['file'] == None:
            return HttpResponse("Not Found File")
        if image.is_valid():
            return handle_encode(request.FILES['file'])
    else:
        image = ImageForm()
        return render(request,"intro.html",{'form':image})


def handle_decode(f):
    upload_decode(f.name,f.read())
    #with open("encoder/static/decode/upload/"+f.name,'wb+') as file:
    #    for chunk in f.chunks():
    #        file.write(chunk)
    file_content = Decode_64(f.name)
    download_decode(f.name,bytes(file_content))
    response = HttpResponse(file_content, content_type='application/*')
    response['Content-Disposition'] = f'attachment; filename="{f.name[:-4]}"'
    return response

def handle_encode(f):
    upload_encode(f.name,f.read())
    #with open("encoder/static/encode/upload/"+f.name,'wb+') as file:
    #    for chunk in f.chunks():
    #        file.write(chunk)
    file_content = Encode_64(f.name)
    download_encode(f.name,bytes(file_content,encoding='utf-8'))
    response = HttpResponse(file_content, content_type='text/*')
    response['Content-Disposition'] = f'attachment; filename="{f.name}.txt"'
    return response
