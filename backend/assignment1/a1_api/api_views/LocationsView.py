from ..api_views.__init__ import *
from ..serializers import LocationSerializer
from ..models import Location

class LocationsView(ListCreateAPIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = LocationSerializer

    def get_queryset(self):
        page_nr = int(self.request.query_params.get('page', 0))
        page_size = int(self.request.query_params.get('size', 15))
        page_start = page_nr * page_size
        return Location.objects.all()[page_start:page_start + page_size]
