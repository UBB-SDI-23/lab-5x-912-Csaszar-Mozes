from ..api_views.__init__ import *
from ..serializers import CompanyNrLocationsSerializer
from ..models import Company
from django.db import models




class CompanyByNrLocationsView(ListAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = CompanyNrLocationsSerializer

    def get_queryset(self):
        page_nr = int(self.kwargs['page_nr'])
        page_size = int(self.kwargs['page_size'])
        page_start = page_nr * page_size
        return Company.objects.all().annotate(nr_comp_locations=models.Count("locations")).\
            order_by("-nr_comp_locations")[page_start:page_start+page_size]
