from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ImpressoraViewSet,
    ImpressoraListView, ImpressoraDetailView, FilaImpressaoListView
)

router = DefaultRouter()
router.register(r'impressoras', ImpressoraViewSet, basename='impressora')

urlpatterns = [
    # API Endpoints
    path('api/', include(router.urls)),
    
    # Template Views
    path('', ImpressoraListView.as_view(), name='impressora-list'),
    path('<int:pk>/', ImpressoraDetailView.as_view(), name='impressora-detail'),
    path('fila/', FilaImpressaoListView.as_view(), name='fila-lista'),
]