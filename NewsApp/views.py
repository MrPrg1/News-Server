from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import NewsModel, NewsSerializer
from rest_framework import permissions


class NewsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        queryset = NewsModel.objects.all()
        serializer = NewsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        title = data['title']
        image = data['image']
        shortDescription = data['shortDescription']
        description = data['description']
        category = data['category']
        dateOfRelease = data['dateOfRelease']
        news = NewsModel(title=title, image=image, shortDescription=shortDescription, description=description, category=category, dateOfRelease=dateOfRelease )
        news.save()
        return Response(status=status.HTTP_200_OK)
    