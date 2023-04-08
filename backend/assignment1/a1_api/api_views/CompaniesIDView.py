from ..api_views.__init__ import *
from ..serializers import CompanySerializer, CompanyDetailSerializer
from ..models import Company


class CompaniesIDView(RetrieveUpdateDestroyAPIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = CompanyDetailSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Company.objects.all()