from ..api_views.__init__ import *
from ..permissions import IsAdministrator
from ..serializers import UserProfileSerializer
from django.contrib.auth.models import User
from ..models import UserProfile


class UserProfileIDView(ListAPIView):
    # add permission to check if user is authenticated
    permission_classes = [IsAdministrator]
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.all()
