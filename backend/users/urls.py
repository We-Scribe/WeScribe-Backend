from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.UsersAPI.as_view(), name='user-list'),
    path("users/<username>/", views.UsersDetailAPI.as_view(), name='user-detail'),
    path("users/<username>/reset-password/", views.UpdatePassword.as_view(), name='update-password')
]
