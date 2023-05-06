from ..api_views.__init__ import *
from ..permissions import *
from ..serializers import PersonWorkingAtCompanyDetailSerializer, PersonWorkingAtCompanySerializer
from ..models import PersonWorkingAtCompany

class PersonCompanyIDView(RetrieveUpdateDestroyAPIView):
    # add permission to check if user is authenticated
    permission_classes = [IsCurrentUserOwner | IsSafeToView | IsModerator | IsAdministrator]
    serializer_class = PersonWorkingAtCompanyDetailSerializer
    lookup_field = "id"

    def get_queryset(self):
        return PersonWorkingAtCompany.objects.all()
