from rest_framework.routers import DefaultRouter
from .views import ArtistaViewSet

router = DefaultRouter()
router.register(r'artistas', ArtistaViewSet)

urlpatterns = router.urls
