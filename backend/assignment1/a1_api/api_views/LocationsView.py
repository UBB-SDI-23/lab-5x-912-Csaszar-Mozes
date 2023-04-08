from ..api_views.__init__ import *
from ..serializers import LocationSerializer
from ..models import Location

class LocationsView(ListCreateAPIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = LocationSerializer

    def get_queryset(self):
        return Location.objects().all()