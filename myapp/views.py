
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import UserModel
from .serializers import UserModelSerializer



@api_view(["GET","POST"])
def person(request):
    if(request.method=="GET"):
        obj=UserModel.objects.all()
        serializer=UserModelSerializer(obj,many=True)
        return Response(serializer.data)
    elif(request.method=="POST"):
        data=request.data
        serializer=UserModelSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)
    elif(request.method=="PUT"):
        data=request.data
        serializer=UserModelSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)
    elif(request.method=="PATCH"):
        data=request.data
        obj=UserModel.objects.get(name=data["name"])
        serializer=UserModelSerializer(obj,data,partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)

# class UserListView(generics.ListCreateAPIView):
#     queryset = UserModel.objects.all()
#     serializer_class = UserModelSerializer

# class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = UserModel.objects.all()
#     serializer_class = UserModelSerializer

# class CreateUserView(generics.CreateAPIView):
#     queryset = UserModel.objects.all()
#     serializer_class = UserModelSerializer
#     def create(self, request, *args, **kwargs):
#         # Extract parameters from the request data
#         username = request.data.get('username')
#         age = request.data.get('age')
#         mark = request.data.get('mark')

#         # Validate parameters
#         if not username or not age or not mark:
#             return Response({'error': 'Missing required parameters'}, status=status.HTTP_400_BAD_REQUEST)

#         # Create a new user with the extracted parameters
#         user_data = {
#             'username': username,
#             'age': age,
#             'mark': mark,
#         }

#         serializer = self.get_serializer(data=user_data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         print("serializer.data",serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)