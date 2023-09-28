from django.urls import path, include
from .views import NewsListView ,NewsUpdateView


urlpatterns = [
    path('news/', NewsListView.as_view()),
    path('NewsUpdate/<int:pk>', NewsUpdateView.as_view()),
]
