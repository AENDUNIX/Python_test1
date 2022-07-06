from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from account.models import UserInfo
from .serializers import UserSerializers, RegisterSerializer, InfoSerializer


class FindViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializers
    filter_backends = [SearchFilter]
    search_fields = ['username']


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class InfoView(generics.CreateAPIView):
    queryset = UserInfo.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = InfoSerializer
