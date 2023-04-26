from rest_framework import generics, permissions

from .models import Notes
from .serializers import NotesSerializer
from .permissions import IsOwnerOrReadOnly

class NotesListAPI(generics.ListCreateAPIView):
    """
    This view provides 'list' of all notes and 'create' new notes.
    """
    serializer_class = NotesSerializer
    queryset = Notes.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NotesDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    """
    This view provides 'retrieve', 'update', 'destroy' actions for the notes to appropriate users.
    """
    serializer_class = NotesSerializer
    queryset = Notes.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserNotesListAPI(generics.ListAPIView):
    serializer_class = NotesSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'username'

    def get_queryset(self):
        query_list = []
        for obj in Notes.objects.all():
            if(obj.user.username == self.kwargs['username']):
                query_list.append(obj)
        return query_list