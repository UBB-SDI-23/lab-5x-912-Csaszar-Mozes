from ..api_views.__init__ import *
from ..permissions import IsSafeToView
from ..serializers import PersonWorkingAtCompanySerializer
from ..models import PersonWorkingAtCompany
from django.db.models import F, Value as V
from django.db.models.functions import Concat

class PersonCompanyView(ListCreateAPIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated | IsSafeToView]
    serializer_class = PersonWorkingAtCompanySerializer

    def get_queryset(self):
        page_nr = int(self.request.query_params.get('page', 0))
        page_size = int(self.request.query_params.get('size', 15))
        page_start = page_nr * page_size
        q_s = PersonWorkingAtCompany.objects.all().order_by('id')[page_start:page_start+page_size]
        q_s = q_s.annotate(persons_name=Concat(F("person__first_name"), V(" "), F("person__last_name")))
        q_s = q_s.annotate(persons_email=F("person__email"))
        q_s = q_s.annotate(company_name=F("company__name"))
        return q_s

    def perform_create(self, serializer):
        serializer.validated_data['user_id'] = self.request.user.id

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)