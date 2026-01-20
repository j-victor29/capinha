from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RecompensaViewSet, UsuarioRecompensaViewSet,
    GamificationDashboardView, BadgesListView, RankingListView
)

router = DefaultRouter()
router.register(r'recompensas', RecompensaViewSet, basename='recompensa')
router.register(r'usuario-recompensas', UsuarioRecompensaViewSet, basename='usuario-recompensa')

urlpatterns = [
    # API Endpoints
    path('api/', include(router.urls)),
    
    # Template Views
    path('', GamificationDashboardView.as_view(), name='gamification-dashboard'),
    path('badges/', BadgesListView.as_view(), name='badges-list'),
    path('ranking/', RankingListView.as_view(), name='ranking-list'),
]