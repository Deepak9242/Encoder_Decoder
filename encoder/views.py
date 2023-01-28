from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from encoder.forms import ImageForm

# Create your views here.
def encode(request):
    template = loader.get_template('intro.html')
    return HttpResponse(template.render())

def upload(request):
    template = loader.get_template('uploaded.html')
    if request.method=='POST':
        image = ImageForm(request.POST,request.FILES)
        if image.is_valid():
            handle_upload(request.FILES['file'])
            return HttpResponse(template.render())
    else:
        image = ImageForm()
        return render(request,"intro.html",{'form':image})

def handle_upload(f):
    with open("encoder/static/upload/"+f.name,'wb+') as file:
        for chunk in f.chunks():
            file.write(chunk)
