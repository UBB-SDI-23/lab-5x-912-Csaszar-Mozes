from ..api_views.__init__ import *
from ..permissions import *
from ..serializers import PersonDetailSerializer
from ..models import Person


class PeopleIDView(RetrieveUpdateDestroyAPIView):
    # add permission to check if user is authenticated
    permission_classes = [IsCurrentUserOwner | IsSafeToView | IsModerator | IsAdministrator]
    serializer_class = PersonDetailSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Person.objects.all()
