from ..api_views.__init__ import *
from ..serializers import LocationDetailSerializer
from ..models import Location


class LocationsIDView(RetrieveUpdateDestroyAPIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = LocationDetailSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Location.objects.all()

