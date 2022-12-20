from django.urls import path, include
from .views import UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r"", UserViewSet, basename="accounts")
urlpatterns = [
    path("login/", obtain_auth_token, name="login"),
    path("", include(router.urls)),
]
