from django.urls import path, include
from .views import NewsView 


urlpatterns = [
    path('news/', NewsView.as_view()),
]
