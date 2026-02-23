from django.db import models

# Create your models here.
class Student(models.Model):
  Name=models.CharField(max_length=100)
  Email=models.EmailField()
  Password=models.CharField(max_length=100)
  Cpassword=models.CharField(max_length=100)


class department(models.Model):
  dname=models.CharField(max_length=100)
  ddes=models.CharField(max_length=100)
  dhead=models.CharField(max_length=100)

class employee(models.Model):
  ename=models.CharField(max_length=100)
  econtact=models.CharField(max_length=100)
  eemail=models.EmailField()
  edep=models.CharField(max_length=100)
  ecode=models.CharField(max_length=100)
  eprofile=models.FileField()