from djongo import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# from django_mongodb_engine.fields import ObjectIdField

# Create your models here.


class UserModel(models.Model):
    username=models.TextField()
    age=models.IntegerField()
    mark=models.FloatField()
    def __str__(self):
        return self.username
    

class Student(models.Model,AbstractUser):
    # id = ObjectIdField(primary_key=True)
    name=models.TextField()
    date=models.DateField()
    dob=models.DateField()
    mobileNumber=models.IntegerField()
    address=models.TextField()
    qualification=models.TextField()
    nationality=models.TextField()
    workingDesignation=models.TextField()
    studentCollegeName=models.TextField()
    email=models.EmailField(unique=True)
    whatsappNumber=models.IntegerField()
    gender=models.TextField()

    USERNAME_FIELD="email"
    REQUIRED_FIELDS = ['name','date']

    @property
    def is_anonymous(self):
        """Always return False. This is a way of comparing User objects to anonymous users. """
        return False
    @property
    def is_authenticated(self):
        """Always return False. This is a way of comparing User objects to anonymous users. """
        return True
    
    def __str__(self):
        return self.name
    
    

    


class Login(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.TextField()
    date=models.DateField()
    
    groups = models.ManyToManyField('auth.Group', related_name='login_users', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='login_users', blank=True)
    REQUIRED_FIELDS = ['name','date']
    


