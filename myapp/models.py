from djongo import models

# from django.db import models

# Create your models here.


class UserModel(models.Model):
    username=models.TextField()
    age=models.IntegerField()
    mark=models.FloatField()
    def __str__(self):
        return self.username
    

class Student(models.Model):
    name=models.TextField()
    date=models.DateField()
    dob=models.DateField()
    mobileNumber=models.IntegerField()
    address=models.TextField()
    qualification=models.TextField()
    nationality=models.TextField()
    workingDesignation=models.TextField()
    studentCollegeName=models.TextField()
    email=models.EmailField()
    whatsappNumber=models.IntegerField()
    gender=models.TextField()
    def __str__(self):
        return self.name
    

    
