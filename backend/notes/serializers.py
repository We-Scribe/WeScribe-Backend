from rest_framework import serializers
from .models import Notes

class NotesSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Notes
        fields = ('id', 'title', 'description', 'user', 'boardID', 'created')