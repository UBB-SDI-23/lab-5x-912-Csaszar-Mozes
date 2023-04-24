from ..api_views.__init__ import *
from ..serializers import CompanyByAvgSalarySerializer
from ..models import Company
import django.db.models as models



class CompanyByAvgSalaryView(ListAPIView):
    #permissions_classes = [permissions.IsAuthenticated]
    serializer_class = CompanyByAvgSalarySerializer
    def get_queryset(self):
        page_nr = int(self.request.query_params.get('page', 0))
        page_size = int(self.request.query_params.get('size', 15))
        page_start = page_nr * page_size
        return Company.objects.all().order_by(
            '-avg_salary')[page_start:page_start+page_size]


# See sql, explain analyze, make sure everything is index-scan
# Write same thing in SQL
# Make company names unique
