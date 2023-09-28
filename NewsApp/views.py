from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import NewsModel, NewsSerializer
from rest_framework import permissions
from rest_framework import generics
from rest_framework import mixins


class NewsListView(mixins.ListModelMixin ,mixins.CreateModelMixin ,generics.GenericAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer

    def get(self, request):
        return self.list(request)
        
    def post(self, request):
        return self.create(request)
    

class NewsUpdateView(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return  self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
    