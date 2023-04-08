from ..api_views.__init__ import *
from ..serializers import PersonWorkingAtCompanySerializer
from ..models import PersonWorkingAtCompany, Person, Company


# url: /people/<person_id:int>/companies/
class PeopleIDCompaniesView(ListCreateAPIView):
    serializer_class = PersonWorkingAtCompanySerializer

    def get_queryset(self):
        return PersonWorkingAtCompany.objects.filter(person=self.kwargs['person_id'])





