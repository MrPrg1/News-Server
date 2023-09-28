from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import NewsModel, NewsSerializer
from rest_framework import permissions
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets

class NewsListView(viewsets.ModelViewSet):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer


