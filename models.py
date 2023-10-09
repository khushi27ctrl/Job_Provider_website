from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122,blank=True,default="00000")
    email=models.CharField(max_length=122,blank=True,default="00000")
    adharcard=models.CharField(max_length=10000,blank=True,default="00000")
    phone=models.CharField(max_length=10000,blank=True,default="00000")
    desc=models.TextField()
    date=models.DateField(auto_now_add=True)
class Registration(models.Model):
    firstname=models.CharField(max_length=122,blank=True,default="00000")
    surname=models.CharField(max_length=122,blank=True,default="00000")
    birthdate=models.CharField(max_length=122,blank=True,default="00000")
    adharcard=models.CharField(max_length=122,blank=True,default="00000")
    passport=models.CharField(max_length=122,blank=True,default="00000")
    martial=models.CharField(max_length=122,blank=True,default="00000")
    email=models.CharField(max_length=122,blank=True,default="00000")
    address=models.CharField(max_length=122,blank=True,default="00000")
    residential=models.CharField(max_length=122,blank=True,default="00000")
    phonenumber=models.CharField(max_length=122,blank=True,default="00000")
    occupation=models.CharField(max_length=122,blank=True,default="00000")
    commencement=models.CharField(max_length=122,blank=True,default="00000")
    income=models.CharField(max_length=122,blank=True,default="00000")
    registered=models.CharField(max_length=122,blank=True,default="00000")
   