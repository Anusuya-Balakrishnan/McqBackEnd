
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
# from knox.models import AuthToken
from rest_framework import status
# from rest_framework import generics
from rest_framework.authtoken.models import Token
from .models import UserModel,Student,CustomUser
from .serializers import UserModelSerializer,StudentSerializer,CustomUserSerializer

# from .emailAuthenticate import EmailBackend

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

@api_view(['GET', 'POST'])
def custom_user_list(request):
    if request.method == 'GET':
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = CustomUser.objects.get(name=request.data['email'])
            print("user$$$$$$$$$$$$$$$$$$$$$",user)
            token="HEllo"
            # _,token=Token.objects.create(user=user)
            return Response({"token":token.key,"user":serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def custom_user_detail(request, name):
    try:
        user = CustomUser.objects.get(name=name)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)