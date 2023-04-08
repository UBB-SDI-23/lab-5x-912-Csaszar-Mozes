from ..api_views.__init__ import *
from ..serializers import PersonSerializer
from ..models import Person


class PeopleView(ListCreateAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = PersonSerializer
    def get_queryset(self):
        page_nr = int(self.kwargs['page_nr'])
        page_size = int(self.kwargs['page_size'])
        page_start = page_nr * page_size
        return Person.objects.all()[page_start:page_start+page_size]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)