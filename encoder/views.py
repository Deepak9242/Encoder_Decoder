from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from encoder.forms import ImageForm
from encoder.encode import Encode_64,Decode_64
from encoder.messenger import sendmessage
from encoder.models import upload_encode,download_encode,upload_decode,download_decode


# Create your views here.
def encode(request):
    template = loader.get_template('intro.html')
    return HttpResponse(template.render())


def email(request):
    if request.method=="POST":
        file_name = request.POST['filename']
        email = request.POST['email']
        print(file_name)
        return HttpResponse(f"send mail to {email} of file {file_name}.")
    else:
        return HttpResponse("invalid")

def decode(request):
    if request.method=='POST':
        if request.FILES['file'].size > 5*1024*1024:
            return HttpResponse("File Size TOO BIG")
        if request.FILES['file'] == None:
            return HttpResponse("No File Found")
        else:
            return handle_decode(request.FILES['file'])



def upload(request):
    template = loader.get_template('uploaded.html')
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
    response = HttpResponse(file_content, content_type='application/*')
    response['Content-Disposition'] = f'attachment; filename="{f.name[:-4]}"'
    return response

def handle_encode(f):
    upload_encode(f.name,f.read())
    #with open("encoder/static/encode/upload/"+f.name,'wb+') as file:
    #    for chunk in f.chunks():
    #        file.write(chunk)
    file_content = Encode_64(f.name)
    response = HttpResponse(file_content, content_type='text/*')
    response['Content-Disposition'] = f'attachment; filename="{f.name}.txt"'
    return response
