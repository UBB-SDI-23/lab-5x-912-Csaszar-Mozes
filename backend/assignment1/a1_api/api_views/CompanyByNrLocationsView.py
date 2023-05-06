from ..api_views.__init__ import *
from ..permissions import IsSafeToView
from ..serializers import CompanyNrLocationsSerializer
from ..models import Company
from django.db import models


class CompanyByNrLocationsView(ListAPIView):
    permissions_classes = [IsSafeToView]
    serializer_class = CompanyNrLocationsSerializer

    def get_queryset(self):
        page_nr = int(self.request.query_params.get('page', 0))
        page_size = int(self.request.query_params.get('size', 15))
        print(self.request.user, self.request.user.id, self.request.user.date_joined, self.request.user.role)
        page_start = page_nr * page_size
        q_s = Company.objects.all().order_by("-nr_locations")[page_start:page_start+page_size]
        return q_s
