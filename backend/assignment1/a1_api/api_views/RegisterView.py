from datetime import timedelta, datetime

from ..api_views.__init__ import *
from ..serializers import RegisterMessageSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterMessageSerializer

    def post(self, request, *args, **kwargs):
        #resp: Response = super().post(request, args=args, kwargs=kwargs)
        user = RegisterSerializer(data=request.data)
        if user.is_valid():
            user.save()
        #change user JSON object to User object
        user = list(User.objects.filter(email=user.data['email']))[0]
        ac = AccessToken.for_user(user)
        expiration_time = datetime.now() + timedelta(minutes=10)
        ac['exp'] = int(expiration_time.timestamp())
        return Response({"activation_token": str(ac)}, status=200)
