from ..api_views.__init__ import *
from ..serializers import LocationDetailSerializer
from ..models import Location
from ..permissions import *


class LocationsIDView(RetrieveUpdateDestroyAPIView):
    # add permission to check if user is authenticated
    permission_classes = [IsCurrentUserOwner | IsSafeToView | IsModerator | IsAdministrator]
    serializer_class = LocationDetailSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Location.objects.all()

