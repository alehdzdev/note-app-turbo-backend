# Third Party
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# Local
from users.serializers import RegisterSerializer


class RegisterView(APIView):
    """Create a new user account."""

    permission_classes = (AllowAny,)

    @extend_schema(
        summary="Register a new user",
        description="Creates a new user account with email and password. No authentication required.",
        request=RegisterSerializer,
        responses={
            201: RegisterSerializer,
            400: OpenApiResponse(description="Validation error"),
        },
        tags=["auth"],
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
