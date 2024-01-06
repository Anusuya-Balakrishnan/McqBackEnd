
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
# from knox.models import AuthToken
from rest_framework import status
# from rest_framework import generics
from rest_framework.authtoken.models import Token
from .models import UserModel,Student,CustomUser
from .serializers import UserModelSerializer,StudentSerializer,CustomUserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
# from .emailAuthenticate import EmailBackend

@api_view(["GET","POST","PATCH"])
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
        print("data",serializer.is_valid())
        if(serializer.is_valid(raise_exception=True)):
            serializer.save()
            user=Student.objects.get(id=request.data["id"])
            print("user",user)
            token=Token.objects.get_or_create(user=user)
            return Response({"token":token.key,"user":serializer.data})
        else:
            return Response({"Error":"invalid user"})
    elif(request.method=="GET"):
        obj=Student.objects.all()
        serializer=StudentSerializer(obj,many=True)
        return Response(serializer.data)



# this api is used to get all user details and register new user 
@api_view(['GET', 'POST'])
def custom_user_list(request):
    if request.method == 'GET':
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        try:
            user = CustomUser.objects.get(email=request.data['email'])
            return Response({"message":"person already present"})
        except:
            serializer = CustomUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                user =CustomUser.objects.get(email=request.data["email"])
                # token="HEllo"
                token, created = Token.objects.get_or_create(user=user)
                return Response({"message":"successfully added into database","token":token.key,"user":serializer.data}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# this api is used for login page of custom user
@api_view(['POST'])
def custom_user_login(request):
    data=request.data
    if request.method=="POST":
        try:
            # user=get_object_or_404(CustomUser,email=data['email'])
            user=CustomUser.objects.get(email=data['email'])
            print("user$$$$$$$$$$$$$$$$$$$$$$$",user)
            serializer = CustomUserSerializer(user)
            print("serializer",serializer)
            token, created = Token.objects.get_or_create(user=user)
            print("token tokentokentokentoken",token.key)
            return Response({"message":"login successfully","token":token.key,"user":serializer.data})
        except:
            return Response({"message":"person not exists"},status=status.HTTP_404_NOT_FOUND)
    

# this api is used to get particular user, update fields of particular user and delete user by name 
@api_view(['GET', 'PATCH', 'DELETE'])
def custom_user_detail(request, name):
    try:
        user = CustomUser.objects.get(name=name)
    except CustomUser.DoesNotExist:
        return Response({"message":"person not exist"},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = CustomUserSerializer(user, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response({"message":"successfully deleted"},status=status.HTTP_204_NO_CONTENT)
    

@api_view(["POST"])
def test_token(request):
    authentication_classes = [TokenAuthentication]
    if(request.method=="POST"):
        data=request.data
       # Retrieve the token from the request
        try:
            token=Token.objects.get(key=request.auth.key)
            user=token.user
            serializer = CustomUserSerializer(user)
            return Response({"message":"token value","token":token.key,"user":serializer.data})
        except:
            return Response({"message":"error"})

        
    