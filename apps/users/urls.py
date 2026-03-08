# Django
from django.urls import path

# Third Party
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Local
from users.views import RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="auth-register"),
    path("login/", TokenObtainPairView.as_view(), name="auth-login"),
    path("refresh/", TokenRefreshView.as_view(), name="auth-refresh"),
]
