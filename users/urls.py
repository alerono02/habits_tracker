from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    # Authorise Tokens
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # API View
    path('registration/', UserCreateAPIView.as_view(), name='registration'),
    path('list/', UserListAPIView.as_view(), name='user_list'),
    path('<str:username>/', UserRetrieveAPIView.as_view(), name='user_detail'),
    path('<str:username>/update/', UserUpdateAPIView.as_view(), name='user_update'),
    path('<str:username>/delete/', UserDestroyAPIView.as_view(), name='user_delete'),

]