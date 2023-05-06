from ..api_views.__init__ import *
from ..permissions import IsSafeToView
from ..serializers import UserProfileSerializer
from ..models import UserProfile


class UserProfileIDView(RetrieveAPIView):
    # add permission to check if user is authenticated
    permission_classes = [IsSafeToView]
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.all()

    def get_object(self):
        try:
            return self.get_queryset().get(id=self.kwargs["id"])
        except UserProfile.DoesNotExist:
            return {"ERROR": "No such user profile found!"}
