from rest_framework import serializers
from .models import UserModel

class UserModelSerializer(serializers.Serializer):
    username=serializers.CharField()
    age=serializers.IntegerField()
    mark=serializers.FloatField()

    def create(self, data):
        return UserModel.objects.create(**data)
