from django.urls import path
from .views import MessageViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'messages', MessageViewSet, basename='messages')
router.register(r'users', UserViewSet, basename='users')
urlpatterns = router.urls
# urlpatterns = [
#     path('messages/', views.getAllMessages),
#     path('messages/readMessage', views.readMessage),
# ]