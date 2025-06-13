from rest_framework_simplejwt.views import TokenObtainPairView

from apps.system.serializers import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    """
    Custom token obtain pair view.
    """
    serializer_class = MyTokenObtainPairSerializer
