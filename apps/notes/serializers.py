# Third Party
from rest_framework import serializers

# Local
from notes.models import Note


class NoteSerializer(serializers.ModelSerializer):
    """Serializer for Note model. Owner is set automatically from the request user."""

    class Meta:
        model = Note
        fields = ("id", "title", "body", "color", "category", "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")
