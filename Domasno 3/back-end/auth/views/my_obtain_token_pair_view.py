from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from auth.serializers import MyTokenObtainPairSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
