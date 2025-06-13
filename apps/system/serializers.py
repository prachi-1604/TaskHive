from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import check_password
from apps.system.messages import INVALID_CREDENTIALS, USER_INACTIVE
from apps.users.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Serializer for obtaining JSON Web Tokens.
    """
    username_field = User.USERNAME_FIELD

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError(INVALID_CREDENTIALS)

        if not check_password(password, user.password):
            raise serializers.ValidationError(INVALID_CREDENTIALS)

        if not user.is_active:
            raise serializers.ValidationError(USER_INACTIVE)

        refresh = self.get_token(user)

        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        data['user'] = {
            'id': user.id,
            'email': user.email,
            'role': user.role,
        }

        return data