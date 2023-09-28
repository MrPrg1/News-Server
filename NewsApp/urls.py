from django.urls import path, include
from .views import NewsListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', NewsListView)

urlpatterns = [
    path('viewsets/', include(router.urls))
]
