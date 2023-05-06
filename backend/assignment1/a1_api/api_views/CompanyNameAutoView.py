from ..api_views.__init__ import *
from ..permissions import IsSafeToView
from ..serializers import CompanySerializer
from ..models import Company
import django.db.models as models



class CompanyNameAutoView(ListAPIView):
    permissions_classes = [IsSafeToView]
    serializer_class = CompanySerializer
    def get_queryset(self):
        page_size = int(self.request.query_params.get('size', 15))
        name = self.request.query_params.get('name', '')
        return Company.objects.filter(name__icontains=name)[:page_size]


# See sql, explain analyze, make sure everything is index-scan
# Write same thing in SQL
# Make company names unique
