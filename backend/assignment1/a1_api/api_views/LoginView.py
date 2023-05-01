from datetime import timedelta, datetime

from ..api_views.__init__ import *
from ..serializers import RegisterMessageSerializer, RegisterSerializer, LoginSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.views import TokenObtainPairView


class LoginView(TokenObtainPairView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

