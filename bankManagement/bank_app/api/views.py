from rest_framework import generics
from bank_app.models import Bank, UserProfile
from bank_app.api.serializers import BankSerializer, UserProfileSerializer

class UserList(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class BankList(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BankDetail(generics.RetrieveAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer