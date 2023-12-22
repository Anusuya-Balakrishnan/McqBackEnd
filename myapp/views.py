from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import UserModel
from .serializers import UserModelSerializer

class UserListView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

class CreateUserView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    def create(self, request, *args, **kwargs):
        # Extract parameters from the request data
        username = request.data.get('username')
        age = request.data.get('age')
        mark = request.data.get('mark')

        # Validate parameters
        if not username or not age or not mark:
            return Response({'error': 'Missing required parameters'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new user with the extracted parameters
        user_data = {
            'username': username,
            'age': age,
            'mark': mark,
        }

        serializer = self.get_serializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        print("serializer.data",serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)