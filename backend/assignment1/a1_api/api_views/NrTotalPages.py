from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView

from ..api_views.__init__ import *
from ..models import Company, Location, Person, PersonWorkingAtCompany
from math import ceil
from ..permissions import IsSafeToView
from ..serializers import NrTotalPagesSerializer


class NrTotalPages(RetrieveAPIView):
    permissions_classes = [IsSafeToView]
    serializer_class = NrTotalPagesSerializer

    def get(self, request, *kwargs):
        page_size = int(request.query_params.get('size', 15))
        url = request.query_params.get('url', 'companies')
        if url.startswith('companies/reputation-greater-than'):
            reputation = int(self.request.query_params.get('reputation', 80))
            qs = Company.objects.filter(reputation__gt=reputation).count()
        elif url.startswith('companies'):
            qs = Company.objects.all().count()
        elif url == 'locations':
            qs = Location.objects.all().count()
        elif url == 'people':
            qs = Person.objects.all().count()
        elif url == 'pc':
            qs = PersonWorkingAtCompany.objects.all().count()
        elif url == 'users':
            qs = User.objects.all().count()
        else:
            return Response({"message": "ERROR: Bad URL provided!"}, 404)
        return Response({"nr_total_pages": ceil(qs/page_size), "nr_results": qs}, 200)
