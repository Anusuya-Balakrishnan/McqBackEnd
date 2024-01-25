
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
# from knox.models import AuthToken
from rest_framework import status
# from rest_framework import generics
from rest_framework.authtoken.models import Token
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
import ast
from collections import OrderedDict
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
           
            token, created = Token.objects.get_or_create(user=user)
            return Response({"message":"login successfully","token":token.key,"user":serializer.data})
        except:
            return Response({"message":"person not exists"},status=status.HTTP_404_NOT_FOUND)
    


@api_view(["POST"])
def custom_user_logout(request):
    if(request.method=="POST"):
        request.user.auth_token.delete()
        return Response({"Message":"logout successfully"})


# this api is used to get particular user, update fields of particular user and delete user by name 
@api_view(['GET', 'PATCH', 'DELETE'])
def custom_user_detail(request, name):
    try:
        user = CustomUser.objects.get(studentName=name)
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


@api_view(['GET','POST'])
def get_mcqList(request):
    try:
        token=Token.objects.get(key=request.auth.key)
        user=token.user
        serializer = CustomUserSerializer(user)
        if(request.method=="GET"):
            mcqListdata = McqListDatatModel.objects.all()
            serializer = McqListDataSerializer(mcqListdata, many=True)
            return Response({"mcqList":serializer.data}) 
        elif(request.method=="POST"):
            try:
                existing_mcqName = McqListDatatModel.objects.get(mcqName=request.data.get('mcqName'))
                return Response({"message": "MCQ already created"})
            except McqListDatatModel.DoesNotExist:
                serializer = McqListDataSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response({"data": serializer.data, "Message": "mcq added successfully"})
                return Response({"Error": "invalid"})
    except CustomUser.DoesNotExist:
        return Response({"Message":"invalid"})

@api_view(['GET'])
def get_languages(request,mcqId):
    try:
        token=Token.objects.get(key=request.auth.key)
        user=token.user
        serializer = CustomUserSerializer(user)
        try:
            if(request.method=="GET"):
                languages = LanguageModel.objects.filter(mcqId=mcqId)
                serializer = LanguageModelSerializer(languages, many=True)
                return Response({"languages":serializer.data}) 
        except:
            return Response({"Message": "error"})
    except CustomUser.DoesNotExist:
        return Response({"Message":"invalid"})



@api_view(['POST'])
def add_languages(request):
    try:
        token=Token.objects.get(key=request.auth.key)
        user=token.user
        serializer = CustomUserSerializer(user)
        if(request.method=="POST"):
            try:
                existing_language = LanguageModel.objects.get(languageName=request.data.get('languageName'))
                return Response({"message": "Language already created"})
            except LanguageModel.DoesNotExist:
                serializer = LanguageModelSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response({"data": serializer.data, "Message": "Language added successfully"})
                return Response({"Message": "error"})
    except :
        return Response({"Message":"invalid"})

@api_view(['GET'])
def get_topic(request,languageId):
    try:
        token=Token.objects.get(key=request.auth.key)
        user=token.user
        serializer = CustomUserSerializer(user)
        try:
            if(request.method=="GET"):
                topic = TopicModel.objects.filter(languageId=languageId)
                serializer = TopicSerializer(topic, many=True)
                return Response({"topic":serializer.data}) 
        except:
            return Response({"Message": "error"})
    except :
        return Response({"Message":"invalid"})


@api_view(['POST'])
def add_topic(request):
    try:
        token=Token.objects.get(key=request.auth.key)
        user=token.user
        serializer = CustomUserSerializer(user)
        if(request.method=="POST"):
            try:
                existing_topicName = TopicModel.objects.get(topicName=request.data.get('topicName'))
                return Response({"message": "Language already created"})
            except TopicModel.DoesNotExist:
                serializer = TopicSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response({"data": serializer.data, "Message": "Language added successfully"})
                return Response({"Message": "error"})
    except :
        return Response({"Message":"invalid"})



@api_view(['POST'])
def add_questions(request):
    try:
        token = Token.objects.get(key=request.auth.key)
        user = token.user
        if request.method == "POST":
            serializer = QuestionSerializer(data=request.data)
            
            if serializer.is_valid():
               print("Validated Data:", serializer.validated_data)
               serializer.save()
               return Response({"data": serializer.data, "Message": "Question added successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"Message": "Validation error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Token.DoesNotExist:
        return Response({"Message": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({"Message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['POST'])
def add_many_questions(request):
    try:
        token = Token.objects.get(key=request.auth.key)
        user = token.user
        if request.method == "POST":
            questions_data = request.data.get('questions', [])

            # Validate and save each question in the list
            responses = []
            for question_data in questions_data:
                serializer = QuestionSerializer(data=question_data)
                if serializer.is_valid():
                    serializer.save()
                    responses.append({"data": serializer.data, "Message": "Question added successfully"})
                else:
                    responses.append({"Message": "Validation error", "errors": serializer.errors})

            return Response(responses, status=status.HTTP_201_CREATED)
    except Token.DoesNotExist:
        return Response({"Message": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({"Message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["GET"])
def get_questions(request, languageId, topicId):
    try:
        token = Token.objects.get(key=request.auth.key)
        user = token.user
        serializer = CustomUserSerializer(user)

        try:
            if request.method == "GET":
                questions = QuestionModel.objects.filter(languageId=languageId, topicId=topicId)
                serializer = QuestionSerializer(questions, many=True)
                questions_values = []
                regular_dict=[]
                id_list=[]
                for item in serializer.data:
                    # get all questions OrderedDict from main data and stored into list
                    regular_dict.append(json.loads(json.dumps(item["questions"])))
                    # get id of each questions
                    id_list.append(item["id"])
                try:
                    for each in regular_dict:
                        ordered_dict = eval(each, {'OrderedDict': OrderedDict})
                        # converting OrderedDict into python dictionary 
                        myDict={}
                        for key, value in ordered_dict.items():
                            myDict[key]=value
                        questions_values.append(myDict)
                except Exception as e:
                    print("error",e)
                result={}
                for id,question in zip(id_list,questions_values):
                    result[id]=question
                resultData={"questions": serializer.data,"questions_values":result}
                return Response({"data":resultData})
        except:
            return Response({"Message": "error"})
    except:
        return Response({"Message": "invalid"})


# @api_view(["GET"])
# def get_questions(request,languageId,topicId):
#     try:
#         token=Token.objects.get(key=request.auth.key)
#         user=token.user
#         serializer = CustomUserSerializer(user)
#         try:
#             if(request.method=="GET"):
#                 questions = QuestionModel.objects.filter(languageId=languageId,topicId=topicId)
#                 serializer = QuestionSerializer(questions, many=True)
#                 # Assuming get_questions_as_dict is a method in your QuestionModel
#                 questions_as_dict_list = [question.get_questions_as_dict() for question in questions]
#                 print("questions_as_dict_list",questions_as_dict_list)
#                 return Response({"questions":serializer.data,"questions_as_dict_list":questions_as_dict_list}) 
#         except:
#             return Response({"Message": "error"})
#     except :
#         return Response({"Message":"invalid"})
