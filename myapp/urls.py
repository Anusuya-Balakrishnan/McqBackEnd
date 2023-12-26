

from django.urls import path
# from .views import UserDetailView,UserListView,CreateUserView
from . import views

urlpatterns = [

    path("user/",views.person,name="person")
#    path('users/', UserListView.as_view(), name='user-list'),
#     path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
#     path('create_user/', CreateUserView.as_view(), name='create-user'),
    # path('custom_create_user/', CreateUserView.as_view({'post': 'create_user'}), name='custom-create-user'),
]
