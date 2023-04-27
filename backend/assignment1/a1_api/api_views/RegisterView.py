from ..api_views.__init__ import *
from ..serializers import RegisterSerializer
from django.contrib.auth.models import User


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
