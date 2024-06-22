from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

urlpatterns = [
    # Users
    path('user/create/', UserCreateAPIView.as_view(), name='user-create'),

    # JWT Tokens endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
