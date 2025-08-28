from rest_framework.routers import DefaultRouter
from .views import ScoreViewSet
router = DefaultRouter()
router.register(r"scores", ScoreViewSet, basename="score")
urlpatterns = router.urls