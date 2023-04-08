from ..api_views.__init__ import *
from ..serializers import PersonWorkingAtCompanySerializer
from ..models import PersonWorkingAtCompany

class PersonCompanyView(ListCreateAPIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = PersonWorkingAtCompanySerializer

    def get_queryset(self):
        page_nr = int(self.kwargs['page_nr'])
        page_size = int(self.kwargs['page_size'])
        page_start = page_nr * page_size
        return PersonWorkingAtCompany.objects.all()[page_start:page_start+page_size]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)