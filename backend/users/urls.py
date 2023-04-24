from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.UsersAPI.as_view(), name='user-list'),
]
