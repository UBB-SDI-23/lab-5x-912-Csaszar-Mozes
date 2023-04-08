from ..api_views.__init__ import *
from ..serializers import CompanySerializer
from ..models import Company

class CompanyReputationGTView(ListAPIView):
    #permissions_classes = [permissions.IsAuthenticated]
    serializer_class = CompanySerializer

    def get_queryset(self):
        reputation = self.kwargs['reputation']
        return Company.objects.filter(reputation__gt=reputation)