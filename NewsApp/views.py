from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import NewsModel, NewsSerializer
from rest_framework import permissions
from rest_framework import generics
from rest_framework import mixins


class NewsListView(generics.ListCreateAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer

    

class NewsUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer

    