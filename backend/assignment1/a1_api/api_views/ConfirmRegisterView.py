import datetime

from rest_framework.request import Request

from ..api_views.__init__ import *
from ..serializers import ConfirmRegisterSerializer
from ..models import Company, UserProfile
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import TokenError
from django.contrib.auth.models import User
import pytz


class ConfirmRegisterView(CreateAPIView):
    serializer_class = ConfirmRegisterSerializer

    def post(self, *args, **kwargs):
        try:
            token = kwargs['token']
            username = self.request.query_params['username']
            user = User.objects.get(username=username)
            user_profile = UserProfile.objects.get(user=user)
            print(datetime.datetime.now(tz=pytz.utc), datetime.timedelta(minutes=10))
            print(user_profile.code_requested_at)
            if token == user_profile.activation_code and user_profile.code_requested_at + datetime.timedelta(minutes=10) > datetime.datetime.now(tz=pytz.utc):
                user.is_active = True
                user.save()
            else:
                return Response({"message": "Bad access token (expired after 10 minutes or invalid)!"})
        except User.DoesNotExist:
            return Response({"message": "No account with given username!"})
        return Response({"message": "Account activated successfully!"}, status=200)
