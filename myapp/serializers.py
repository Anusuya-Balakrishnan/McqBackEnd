from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import UserModel,Student

# User = get_user_model()

# class EmailAuthTokenSerializer(AuthTokenSerializer):
#     def validate(self, attrs):
#         email = attrs.get('email')
        

#         if email :
#             user = User.objects.filter(email=email).first()
#             if user:
#                 attrs['user'] = user
#             else:
#                 msg = 'Unable to log in with provided credentials.'
#                 raise serializers.ValidationError(msg)
#         else:
#             msg = 'Must include "email" and "password".'
#             raise serializers.ValidationError(msg)

#         return attrs

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



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name=serializers.CharField()
    date=serializers.DateField()

    def validate_email(self, email):
        user = get_user_model()
        # print(user)
        print("sdfdassdafsafas",user.get_email_field_name)
        # Check if the email is unique in your database
        print( user.objects.filter(email=email).exists())
        if user.objects.filter(email=email).exists():
            print("Hello")
            # raise serializers.ValidationError("This email is already in use.")

        # Add any other custom validation logic here

        return user
    def create(self, validated_data):
        # Create and return a new user instance using the validated data
        return get_user_model().objects.create(**validated_data)



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