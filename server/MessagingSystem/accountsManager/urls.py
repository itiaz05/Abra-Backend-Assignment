from .views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'accounts', UserViewSet, basename='accounts')
urlpatterns = router.urls
