from ..api_views.__init__ import *
from ..serializers import PersonWorkingAtCompanySerializer
from ..models import PersonWorkingAtCompany
from ..permissions import *


class CompaniesIDPeopleIDView(RetrieveUpdateDestroyAPIView):
    serializer_class = PersonWorkingAtCompanySerializer
    permission_classes = [IsCurrentUserOwner | IsSafeToView | IsModerator | IsAdministrator]
    def get_queryset(self):
        return PersonWorkingAtCompany.objects.all()

    def get_object(self):
        return get_object_or_404(self.get_queryset(), person=self.kwargs['person_id'], company=self.kwargs['comp_id'])

    def perform_update(self, serializer):
        pc = get_object_or_404(self.get_queryset(), person=self.kwargs['person_id'], company=self.kwargs['comp_id'])
        ser_data = {
            'salary': self.request.data.get('salary'),
            'role': self.request.data.get('role'),
        }
        ser = PersonWorkingAtCompanySerializer(instance=pc,data=ser_data,partial=True)
        if ser.is_valid():
            ser.save()