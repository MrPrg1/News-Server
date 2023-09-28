from django.urls import path, include
from .views import NewsListView, UserListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', NewsListView)

urlpatterns = [
    path('viewsets/', include(router.urls)),
    path('users/', UserListView.as_view())
]
