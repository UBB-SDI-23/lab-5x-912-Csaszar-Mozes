from ..api_views.__init__ import *
from ..serializers import PersonWorkingAtCompanySerializer
from ..models import PersonWorkingAtCompany



# url: /companies/<comp_id:int>/people/
class CompaniesIDPeopleView(ListCreateAPIView):
    serializer_class = PersonWorkingAtCompanySerializer

    def get_queryset(self):
        return PersonWorkingAtCompany.objects.filter(company=self.kwargs['comp_id'])