# Django
from django.urls import path

# Third Party
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Local
from users.views import RegisterView

TokenObtainPairView = extend_schema(
    summary="Login",
    description="Obtain a JWT access and refresh token pair using email and password.",
    tags=["auth"],
)(TokenObtainPairView)

TokenRefreshView = extend_schema(
    summary="Refresh token",
    description="Obtain a new access token using a valid refresh token.",
    tags=["auth"],
)(TokenRefreshView)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="auth-register"),
    path("login/", TokenObtainPairView.as_view(), name="auth-login"),
    path("refresh/", TokenRefreshView.as_view(), name="auth-refresh"),
]
