from ..api_views.__init__ import *
from ..serializers import CompanyByAvgSalarySerializer
from ..models import Company
import django.db.models as models



class CompanyByAvgSalaryView(ListAPIView):
    #permissions_classes = [permissions.IsAuthenticated]
    serializer_class = CompanyByAvgSalarySerializer
    def get_queryset(self):
        page_nr = int(self.kwargs['page_nr'])
        page_size = int(self.kwargs['page_size'])
        page_start = page_nr * page_size
        return Company.objects.all().annotate(avg_salary=models.Avg('people_working_here__salary', default=0)).order_by(
            '-avg_salary')[page_start:page_start+page_size]