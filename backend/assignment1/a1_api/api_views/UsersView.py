from ..api_views.__init__ import *
from ..permissions import IsAdministrator
from ..serializers import UserProfileSerializer
from django.contrib.auth.models import User
from ..models import UserProfile


class UsersView(ListAPIView):
    # add permission to check if user is authenticated
    permission_classes = [IsAdministrator]
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        page_nr = int(self.request.query_params.get('page', 0))
        page_size = int(self.request.query_params.get('size', 15))

        page_start = page_nr * page_size
        return UserProfile.objects.all()[page_start:page_start+page_size]
