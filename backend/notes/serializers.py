from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Notes

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ('id', 'user', 'content')