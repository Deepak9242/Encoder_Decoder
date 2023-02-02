from django.http import HttpResponse, HttpResponseNotFound
import base64
from encoder.models import DecodedDataUpload,EncodedDataUpload,EncodedDataDownload,download_encode

def Encode_64(filename):
    file_path = f"encoder/static/encode/upload/{filename}"
    record = EncodedDataUpload.objects.filter(name=filename)
    #tex = open(file_path,'rb+')
    tex = record.values()[0]['data']
    bytes = base64.b64encode(bytearray(tex))
    file_content = bytes.decode("ascii")

    download_encode(filename,bytes)
    #save_path = f"encoder/static/encode/download/{filename}.txt"
    #with open(save_path,'w+') as file:
    #    file.write(file_content)
    #    file.close()
    return file_content

def Decode_64(filename):
    file_path = f"encoder/static/decode/upload/{filename}"
    print(filename)
    record = DecodedDataUpload.objects.filter(name=filename)
    #tex = open(file_path,'rb+')
    tex = record.values()[0]['data']
    bytes = base64.b64decode(bytearray(tex))
    return bytes

#tex = Image.open(r"encodeimage.jpg").convert("RGBA").resize((100,100))
#print(tex.size)
#bytes = base64.b64encode(tex.tobytes())

#file_content = bytes.decode("ascii")

#img = base64.b64decode(bytes)
#img_pil = Image.frombytes("RGBA",(100,100),img)
#img_pil.show()

#with open("encoded.txt","w") as file:
#    file.write(file_content)
#    file.close()
