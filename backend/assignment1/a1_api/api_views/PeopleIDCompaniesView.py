from ..api_views.__init__ import *
from ..serializers import PersonWorkingAtCompanySerializer
from ..models import PersonWorkingAtCompany, Person, Company


# url: /people/<person_id:int>/companies/
class PeopleIDCompaniesView(ListCreateAPIView):
    serializer_class = PersonWorkingAtCompanySerializer

    def get_queryset(self):
        return PersonWorkingAtCompany.objects.filter(person=self.kwargs['person_id'])

    def perform_create(self, serializer):
        ser_data = {
            'salary': self.request.data.get('salary'),
            'role': self.request.data.get('role'),
            'person': self.request.data.get('person_id'),
            'company': self.kwargs.get('company')
        }
        ser = PersonWorkingAtCompanySerializer(data=ser_data)
        if ser.is_valid():
            ser.save()





