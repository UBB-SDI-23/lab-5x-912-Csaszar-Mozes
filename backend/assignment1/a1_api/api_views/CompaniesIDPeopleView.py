from ..api_views.__init__ import *
from ..permissions import IsCurrentUserOwner
from ..serializers import PersonWorkingAtCompanySerializer
from ..models import PersonWorkingAtCompany



# url: /companies/<comp_id:int>/people/
class CompaniesIDPeopleView(ListCreateAPIView):
    serializer_class = PersonWorkingAtCompanySerializer
    permission_classes = [IsCurrentUserOwner | permissions.IsAuthenticated]

    def get_queryset(self):
        return PersonWorkingAtCompany.objects.filter(company=self.kwargs['comp_id'])

    def perform_create(self, serializer):
        ser_data = {
            'salary': self.request.data.get('salary'),
            'role': self.request.data.get('role'),
            'person': self.request.data.get('person'),
            'company': self.kwargs.get('comp_id')
        }
        ser = PersonWorkingAtCompanySerializer(data=ser_data)
        if ser.is_valid():
            ser.save()
