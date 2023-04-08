from ..api_views.__init__ import *
from ..serializers import PersonSerializer, PersonDetailSerializer
from ..models import Person


class PeopleIDView(RetrieveUpdateDestroyAPIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = PersonDetailSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Person.objects().all()
