from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PedidoViewSet, ItemPedidoViewSet,
    PedidoListView, PedidoDetailView
)

router = DefaultRouter()
router.register(r"orders", PedidoViewSet, basename="orders")

urlpatterns = [
    # API Endpoints
    path("api/", include(router.urls)),
    path(
        "api/orders/items/<int:pk>/",
        ItemPedidoViewSet.as_view({"put": "update", "delete": "destroy"}),
        name="order-item-detail",
    ),
    
    # Template Views
    path("", PedidoListView.as_view(), name="pedido-list"),
    path("<int:pk>/", PedidoDetailView.as_view(), name="pedido-detail"),
]