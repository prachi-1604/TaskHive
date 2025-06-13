from rest_framework import generics, status
from rest_framework.response import Response

from apps.users.serializers import UserRegisterSerializer
from apps.users.messages import USER_REGISTERED_SUCCESSFULLY

class RegisterView(generics.CreateAPIView):
    """
    API endpoint for user registration.
    """
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            "success": True,
            "message": USER_REGISTERED_SUCCESSFULLY,
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)
