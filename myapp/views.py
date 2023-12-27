
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import UserModel,Student
from .serializers import UserModelSerializer,StudentSerializer,StudentSignInSerializer
from rest_framework.authtoken.models import Token



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


# http://127.0.0.1:8000/mcq/student/
# this api is used to create a student using post method
# using the same api ,we can get all student data by using get method
@api_view(["POST","GET"])
def student(request):
    if(request.method=="POST"):
        data=request.data
        serializer=StudentSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"Error":"invalid user"})
    elif(request.method=="GET"):
        obj=Student.objects.all()
        serializer=StudentSerializer(obj,many=True)
        return Response(serializer.data)

@api_view(["POST"])
def studentLogin(request):
    if(request.method=="POST"):
        serializer = StudentSignInSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        token, created = Token.objects.get_or_create(user=email)

        return Response({'token': token.key}, status=status.HTTP_200_OK)



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