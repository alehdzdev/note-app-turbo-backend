# Third Party
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter, OpenApiResponse
from drf_spectacular.types import OpenApiTypes
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

# Local
from notes.models import Note
from notes.serializers import NoteSerializer


@extend_schema_view(
    list=extend_schema(
        summary="List notes",
        description="Returns all notes belonging to the authenticated user. Optionally filter by category.",
        parameters=[
            OpenApiParameter(
                name="category",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Filter notes by category.",
                required=False,
            )
        ],
        responses={200: NoteSerializer(many=True)},
        tags=["notes"],
    ),
    create=extend_schema(
        summary="Create a note",
        description="Creates a new note owned by the authenticated user.",
        request=NoteSerializer,
        responses={201: NoteSerializer, 400: OpenApiResponse(description="Validation error")},
        tags=["notes"],
    ),
    retrieve=extend_schema(
        summary="Retrieve a note",
        description="Returns a single note by ID, scoped to the authenticated user.",
        responses={200: NoteSerializer, 404: OpenApiResponse(description="Not found")},
        tags=["notes"],
    ),
    update=extend_schema(
        summary="Update a note",
        description="Partially updates a note by ID. All fields are optional.",
        request=NoteSerializer,
        responses={200: NoteSerializer, 400: OpenApiResponse(description="Validation error"), 404: OpenApiResponse(description="Not found")},
        tags=["notes"],
    ),
    partial_update=extend_schema(exclude=True),
)
class NoteViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    """ViewSet for listing, creating, retrieving, and updating notes scoped to the request user."""

    serializer_class = NoteSerializer

    def get_queryset(self):
        queryset = Note.objects.filter(owner=self.request.user)
        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(category=category)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)

    def handle_exception(self, exc):
        response = super().handle_exception(exc)
        if isinstance(response.data, dict) and "detail" in response.data:
            response.data = {"error": str(response.data["detail"])}
        return response
