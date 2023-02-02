from django.http import HttpResponse, HttpResponseNotFound
import base64


def Encode_64(filename):
    file_path = f"encoder/static/encode/upload/{filename}"
    tex = open(file_path,'rb+')
    bytes = base64.b64encode(bytearray(tex.read()))
    file_content = bytes.decode("ascii")
    save_path = f"encoder/static/encode/download/{filename}.txt"
    with open(save_path,'w+') as file:
        file.write(file_content)
        file.close()
    return file_content

def Decode_64(filename):
    file_path = f"encoder/static/decode/upload/{filename}"
    tex = open(file_path,'rb+')
    bytes = base64.b64decode(bytearray(tex.read()))
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
