from ..api_views.__init__ import *
from ..serializers import CompanyNrLocationsSerializer
from ..models import Company
from django.db import models


class CompanyByNrLocationsView(ListAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = CompanyNrLocationsSerializer

    def get_queryset(self):
        page_nr = int(self.request.query_params.get('page', 0))
        page_size = int(self.request.query_params.get('size', 15))
        page_start = page_nr * page_size
        q_s = Company.objects.all().annotate(nr_company_locations=models.Count("locations")).\
            order_by("-nr_company_locations")[page_start:page_start+page_size]
        return q_s
