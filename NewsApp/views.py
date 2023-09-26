from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import NewsModel, NewsSerializer
from rest_framework import permissions


class NewsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get_object(self,):
        try:
            news = NewsModel.objects.all()
            return news
        except:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        news = self.get_object()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)
    