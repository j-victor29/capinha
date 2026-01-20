from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet, payment_list_view, payment_detail_view

router = DefaultRouter()
router.register(r"payments", PaymentViewSet, basename="payments")

urlpatterns = [
    # Rotas HTML (templates)
    path('', payment_list_view, name='payment-list'),
    path('<int:pk>/', payment_detail_view, name='payment-detail'),
    
    # Rotas API REST
    path('api/', include(router.urls)),
]
