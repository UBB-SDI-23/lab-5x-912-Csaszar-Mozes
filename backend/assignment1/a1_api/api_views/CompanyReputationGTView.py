from ..api_views.__init__ import *
from ..serializers import CompanySerializer
from ..models import Company

class CompanyReputationGTView(ListAPIView):
    #permissions_classes = [permissions.IsAuthenticated]
    serializer_class = CompanySerializer

    def get_queryset(self):
        reputation = self.kwargs['reputation']
        page_nr = int(self.request.query_params.get('page', 0))
        page_size = int(self.request.query_params.get('size', 15))
        page_start = page_nr * page_size
        return Company.objects.filter(reputation__gt=reputation)[page_start:page_start+page_size]