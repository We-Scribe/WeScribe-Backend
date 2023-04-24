from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from users.models import CustomUser
from users.serializers import UserRegistrationSerializer


class UsersAPI(generics.ListCreateAPIView):
    """
    This view provides 'list' for all users and 'create' new users.
    """
    serializer_class = UserRegistrationSerializer
    queryset = CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                details = serializer.data
                details['token'] = token.key
                return Response(details, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)