from ..api_views.__init__ import *
from ..serializers import PersonWorkingAtCompanySerializer
from ..models import PersonWorkingAtCompany



# url: /people/<person_id:int>/companies/<comp_id:int>/
class PeopleIDCompaniesIDView(RetrieveUpdateDestroyAPIView):
    serializer_class = PersonWorkingAtCompanySerializer

    def get_queryset(self):
        return PersonWorkingAtCompany.objects.all()

    def get_object(self):
        return get_object_or_404(self.get_queryset(), person=self.kwargs['person_id'], company=self.kwargs['comp_id'])
