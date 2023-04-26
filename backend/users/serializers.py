from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'username',
                  'email', 'password')
        write_only_fields = ('password',)

    #To store password in hash format we need to overwrite create and update functions
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(UserRegistrationSerializer, self).update(instance, validated_data)


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'username',
                  'email', 'password')
        read_only_fields = ('username', 'email', 'password')


class UpdatePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
