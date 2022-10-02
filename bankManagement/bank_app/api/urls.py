from django.urls import path
from bank_app.api.views import BankList, BankDetail, UserList, UserDetail

urlpatterns = [
    path('userlist/', UserList.as_view(), name='userlist'),
    path('userlist/<str:pk>/', UserDetail.as_view(), name='userdetail'),
    path('banklist/', BankList.as_view(), name='banklist'),
    path('banklist/<str:pk>/', BankDetail.as_view(), name='bankdetail'),
]