from rest_framework import generics

from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """
    Представление, создания пользователя.
    """
    serializer_class = UserSerializer
