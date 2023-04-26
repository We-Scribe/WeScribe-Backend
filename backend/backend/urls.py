from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.api_root, name='home'), #Home page of API root
    path('', include('users.urls')),
    path('', include('notes.urls')),
    path('api/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
]
