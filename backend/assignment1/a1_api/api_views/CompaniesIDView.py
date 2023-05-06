from ..api_views.__init__ import *
from ..serializers import CompanySerializer, CompanyDetailSerializer
from ..models import Company
from ..permissions import *


class CompaniesIDView(RetrieveUpdateDestroyAPIView):
    # add permission to check if user is authenticated
    permission_classes = [IsCurrentUserOwner | IsSafeToView | IsModerator | IsAdministrator]
    serializer_class = CompanyDetailSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Company.objects.all()
