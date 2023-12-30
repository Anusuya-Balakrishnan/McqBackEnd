from rest_framework import serializers
from .models import UserModel,Student
from django.contrib.auth import authenticate

from django.contrib.auth import get_user_model
from knox.auth import TokenAuthentication

User = get_user_model()

class EmailAuthTokenSerializer(AuthTokenSerializer):
    def validate(self, attrs):
        email = attrs.get('email')
        

        if email :
            user = User.objects.filter(email=email).first()
            if user:
                attrs['user'] = user
            else:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg)

        return attrs

class UserModelSerializer(serializers.Serializer):
    username=serializers.CharField()
    age=serializers.IntegerField()
    mark=serializers.FloatField()

    def create(self, data):
        return UserModel.objects.create(**data)

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField()
    date=serializers.DateField()
    dob=serializers.DateField()
    mobileNumber=serializers.IntegerField()
    address=serializers.CharField()
    qualification=serializers.CharField()
    nationality=serializers.CharField()
    workingDesignation=serializers.CharField()
    studentCollegeName=serializers.CharField()
    email=serializers.EmailField()
    whatsappNumber=serializers.IntegerField()
    gender=serializers.CharField()
    def create(self, data):
        return Student.objects.create(**data)



class SiginSerializer(serializers.Serializer):
    email = serializers.EmailField()


# class StudentSignInSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)

#     def validate(self, data):
#         email = data.get('email')
#         password = data.get('password')

#         if email and password:
#             user = authenticate(request=self.context.get('request'), email=email, password=password)

#             if not user:
#                 msg = 'Unable to log in with provided credentials.'
#                 raise serializers.ValidationError(msg, code='authorization')

#         else:
#             msg = 'Must include "email" and "password".'
#             raise serializers.ValidationError(msg, code='authorization')

#         data['user'] = user
#         return data