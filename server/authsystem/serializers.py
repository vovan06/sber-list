from rest_framework import serializers
from .models import User


class StartPasswordRestoreSerializer(serializers.Serializer):
    email = serializers.EmailField()

class PasswordRestoreSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class LoginRequestSerializer(serializers.ModelSerializer):
    '''Login serializer. Including name, surname, email, password, is_superuser, is_staff'''
    password = serializers.CharField(
        max_length=256
    )

    class Meta:
        model = User
        fields = ("email", 'password', 'telegram_user_id')

class LoginSerializer(serializers.ModelSerializer):
    '''Login serializer. Including name, surname, email, password, is_superuser, is_staff'''
    id = serializers.UUIDField()
    password = serializers.CharField(
        max_length=256
    )

    class Meta:
        model = User
        fields = ("__all__")

class RegisterSerializer(serializers.ModelSerializer):
    '''Register serializer. Including name, surname, email, password, is_superuser, is_staff'''
    password = serializers.CharField(
        max_length=256
    )
    
    class Meta:
        model = User
        fields = ("__all__")

    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserPatchingSerializer(serializers.ModelSerializer):
    '''Serializer for user patching. Including name, surname, email, password, is_superuser, is_staff'''
    class Meta:
        model = User
        fields = "__all__"

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)