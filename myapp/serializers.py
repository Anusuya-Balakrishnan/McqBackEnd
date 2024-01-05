from rest_framework import serializers
# from django.contrib.auth import get_user_model

from .models import UserModel,Student,CustomUser

class UserModelSerializer(serializers.Serializer):
    username=serializers.CharField()
    age=serializers.IntegerField()
    mark=serializers.FloatField()

    def create(self, data):
        return UserModel.objects.create(**data)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
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
    
class CustomUserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        fields = ('id', 'name', 'date', 'dob', 'mobileNumber', 'address', 'qualification',
                  'nationality', 'workingDesignation', 'studentCollegeName', 'email',
                  'whatsappNumber', 'gender', 'is_active', 'is_staff')
        read_only_fields = ('id', 'is_active', 'is_staff')
    def get_id(self, obj):
        # Convert the Djongo ObjectId to a string
        return str(obj.id)