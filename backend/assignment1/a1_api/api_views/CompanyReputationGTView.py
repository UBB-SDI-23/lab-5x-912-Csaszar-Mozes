from ..api_views.__init__ import *
from ..serializers import CompanySerializer
from ..models import Company

class CompanyReputationGTView(ListAPIView):
    #permissions_classes = [permissions.IsAuthenticated]
    serializer_class = CompanySerializer

    def get_queryset(self):
        page_nr = int(self.request.query_params.get('page', 0))
        page_size = int(self.request.query_params.get('size', 15))
        reputation = int(self.request.query_params.get('reputation', 80))
        page_start = page_nr * page_size
        qs = Company.objects.filter(reputation__gt=reputation)[page_start:page_start+page_size]
        print(qs.query)
        return qs