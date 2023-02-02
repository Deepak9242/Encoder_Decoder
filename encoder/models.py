from django.db import models

# Create your models here.
def upload_encode(name,data):
    temp = EncodedDataUpload(name=name,data=data)
    temp.save()

def download_encode(name,data):
    temp = EncodedDataDownload(name=name,data=data)
    temp.save()

def upload_decode(name,data):
    temp = DecodedDataUpload(name=name,data=data)
    temp.save()

def download_decode(name,data):
    temp = DecodedDataDownload(name=name,data=data)
    temp.save()

class EncodedDataUpload(models.Model):
    name = models.CharField(max_length=255)
    data = models.BinaryField()

class EncodedDataDownload(models.Model):
    name = models.CharField(max_length=255)
    data = models.BinaryField()

class DecodedDataUpload(models.Model):
    name = models.CharField(max_length=255)
    data = models.BinaryField()

class DecodedDataDownload(models.Model):
    name = models.CharField(max_length=255)
    data = models.BinaryField()
