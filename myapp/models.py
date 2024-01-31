# from django.db import models

from djongo import models
import json

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
    
# class CustomUserManager(BaseUserManager):
#     def create_user(self, oceanRegisterNo,email, password=None,**extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(oceanRegisterNo=oceanRegisterNo, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self,oceanRegisterNo, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(oceanRegisterNo,email, password, **extra_fields)


class CustomUserManager(BaseUserManager):
    def create_user(self, oceanRegisterNo, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(oceanRegisterNo=oceanRegisterNo, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, oceanRegisterNo, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Call the base class create_superuser method
        return super().create_superuser(oceanRegisterNo, email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    studentName = models.TextField()
    oceanRegisterNo=models.TextField(unique=True)
    mobileNumber = models.TextField()
    email = models.EmailField()
    password=models.TextField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'oceanRegisterNo'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.oceanRegisterNo

class McqListDatatModel(models.Model):
    mcqName=models.TextField()
    def __str__(self):
        return self.mcqName

class LanguageModel(models.Model):
    mcqId=models.ForeignKey(McqListDatatModel,on_delete=models.CASCADE)
    languageName=models.TextField()
    def __str__(self):
        return self.languageName
    
class TopicModel(models.Model):
    languageId=models.ForeignKey(LanguageModel, on_delete=models.CASCADE)
    topicName=models.TextField()
    def __str__(self):
        return self.topicName
    
class QuestionModel(models.Model):
    languageId=models.ForeignKey(LanguageModel, on_delete=models.CASCADE)
    topicId=models.ForeignKey(TopicModel,on_delete=models.CASCADE)
    questions=models.JSONField()
    level=models.TextField()
    mark=models.IntegerField()
    time=models.IntegerField()
    def get_questions_as_dict(self):
        return json.loads(self.questions)

class ResultModel(models.Model):
    userID=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    languageId=models.ForeignKey(LanguageModel, on_delete=models.CASCADE)
    topicId=models.ForeignKey(TopicModel,on_delete=models.CASCADE)
    answeredQuestions=models.JSONField()
    result=models.IntegerField()
    level=models.TextField()
    # currentDate=models.DateField()
    # noOfTimeAttended=models.IntegerField()