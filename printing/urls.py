from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImpressoraViewSet

router = DefaultRouter()
router.register(r'impressoras', ImpressoraViewSet, basename='impressora')

urlpatterns = [
    path('', include(router.urls)),
]