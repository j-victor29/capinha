from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, user_list_view

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')

urlpatterns = [
    path('', user_list_view, name='user_list'),
    path('api/', include(router.urls)),
]