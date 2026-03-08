# Third Party
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

# Local
from notes.models import Note
from notes.serializers import NoteSerializer


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
