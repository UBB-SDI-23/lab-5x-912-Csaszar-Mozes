from ..api_views.__init__ import *
from ..serializers import CompanyNrLocationsSerializer
from ..models import Company
from django.db import models




class CompanyByNrLocationsView(ListAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = CompanyNrLocationsSerializer

    def get_queryset(self):
        companies = Company.objects.all().annotate(nr_comp_locations=models.Count("locations")).order_by("-nr_comp_locations")
        return companies
