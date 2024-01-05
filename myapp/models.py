from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser, BaseUserManager, PermissionsMixin


# Create your models here.


class UserModel(models.Model):
    username=models.TextField()
    age=models.IntegerField()
    mark=models.FloatField()
    def __str__(self):
        return self.username
    

class Student(models.Model):
    
    name=models.TextField()
    date=models.DateTimeField()
    dob=models.DateTimeField()
    mobileNumber=models.TextField()
    address=models.TextField()
    qualification=models.TextField()
    nationality=models.TextField()
    workingDesignation=models.TextField()
    studentCollegeName=models.TextField()
    email=models.EmailField()
    whatsappNumber=models.TextField()
    gender=models.TextField()

   
    def __str__(self):
        return self.name
    
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.TextField()
    date = models.DateTimeField()
    dob = models.DateTimeField()
    mobileNumber = models.TextField()
    address = models.TextField()
    qualification = models.TextField()
    nationality = models.TextField()
    workingDesignation = models.TextField()
    studentCollegeName = models.TextField()
    email = models.EmailField(unique=True)
    whatsappNumber = models.TextField()
    gender = models.TextField()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    
