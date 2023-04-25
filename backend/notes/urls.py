from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.NotesListAPI.as_view(), name='notes-list'),
    path("notes/details/<int:pk>/", views.NotesDetailAPI.as_view(), name='notes-detail'),
    path("users/<username>/notes/", views.UserNotesListAPI.as_view(), name='users-notes'),
]
