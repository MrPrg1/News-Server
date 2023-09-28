from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import NewsModel, NewsSerializer, UserSerializer
from rest_framework import permissions
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


User = get_user_model()

class NewsListView(viewsets.ModelViewSet):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    pagination_class = PageNumberPagination
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]




class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer