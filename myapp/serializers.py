from rest_framework import serializers

# from django.contrib.auth import get_user_model

from .models import *

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
        fields = ('id', 'studentName', 'date', 'dob', 'mobileNumber', 'address', 'qualification',
                  'nationality', 'workingDesignation', 'studentCollegeName', 'email',
                  'whatsappNumber', 'gender', 'is_active', 'is_staff')
        read_only_fields = ('id', 'is_active', 'is_staff')
    def get_id(self, obj):
        # Convert the Djongo ObjectId to a string
        return str(obj.id)
    

class McqListDataSerializer(serializers.ModelSerializer):
     class Meta:
        model = McqListDatatModel
        fields = '__all__'

class LanguageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageModel
        fields = '__all__'  

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicModel
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=QuestionModel
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model=ResultModel
        fields="__all__"