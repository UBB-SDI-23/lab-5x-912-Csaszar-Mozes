from rest_framework.request import Request

from ..api_views.__init__ import *
from ..serializers import ConfirmRegisterSerializer
from ..models import Company
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import TokenError
from django.contrib.auth.models import User


class ConfirmRegisterView(CreateAPIView):
    serializer_class = ConfirmRegisterSerializer

    def post(self, *args, **kwargs):
        try:
            token = kwargs['token']
            ac = AccessToken(token)
            user_id = ac.get('user_id')
            user = list(User.objects.filter(id=user_id))[0]
            user.is_active = True
            user.save()
        except TokenError:
            return Response({"message": "Bad access token (expired after 10 minutes or invalid)!"})
        return Response({"message": "Account activated successfully!"}, status=200)


    # def perform_create(self, serializer):
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)