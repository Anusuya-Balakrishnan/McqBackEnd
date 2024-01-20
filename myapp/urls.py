

from django.urls import path
# from .views import UserDetailView,UserListView,CreateUserView
from . import views

urlpatterns = [

    path("user/",views.person,name="person"),
    path("student/",views.student,name="student"),
    path('users/', views.custom_user_list, name='custom_user_list'),
    path("userLogin/",views.custom_user_login,name='custom_login'),
    path("userLogout/",views.custom_user_logout,name="custom_logout"),
    path("test_token/",views.test_token,name="test_token"),
    path("get_mcqList/",views.get_mcqList,name="get_mcqList"),
    path('add_languages/',views.add_languages,name='add_languages'),
    path('get_language/<int:mcqId>/',views.get_languages,name='get_languages'),
    path('add_topic/',views.add_topic,name='add_topic'),
    path('get_topic/<int:languageId>/',views.get_topic,name='get_topic'),
    path('add_questions/',views.add_questions,name="add_questions"),
    path('add_many_questions/',views.add_many_questions,name="add_many_questions"),
    path('get_questions/<int:languageId>/<int:topicId>/',views.get_questions,name='get_questions'),
    path('users/<str:name>/', views.custom_user_detail, name='custom_user_detail'),
]

# {
# "studentName":"siva",
# "date":"2022-01-18T12:30:45.123Z",
# "dob":"1990-05-15T08:00:00+02:00",
# "mobileNumber":"9489645465",
# "address":"pondy",
# "qualification":"B.Tech",
# "nationality":"Indian",
# "workingDesignation":"developer",
# "studentCollegeName":"christ",
# "email":"siva@gmail.com",
# "whatsappNumber":"9489645465",
# "gender":"male"
# }

# {"languageId":1,
# "topicId":1,
# "questions":{"question":"Who invented Java Programming?","option":["Guido van Rossum","James Gosling","Dennis Ritchie","Bjarne Stroustrup"],"answer":"James Gosling"},
# "level":"beginner",
# "mark":1,
# "time":1
# }