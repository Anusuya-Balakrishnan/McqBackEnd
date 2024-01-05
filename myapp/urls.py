

from django.urls import path
# from .views import UserDetailView,UserListView,CreateUserView
from . import views

urlpatterns = [

    path("user/",views.person,name="person"),
    path("student/",views.student,name="student"),
    path('users/', views.custom_user_list, name='custom_user_list'),
    path('users/<str:name>/', views.custom_user_detail, name='custom_user_detail'),
]


# {
# "name":"siva",
# "date":"2024-01-05",
# "dob":"1995-12-26",
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
