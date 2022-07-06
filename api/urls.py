from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import FindViewSet, RegisterView, InfoView

router = SimpleRouter()

router.register(r'names', FindViewSet, basename='find')


urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('register-info/', InfoView.as_view(), name='register_nfo'),
]
urlpatterns += router.urls