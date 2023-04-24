from ..api_views.__init__ import *
from ..serializers import CompanySerializer
from ..models import Company

class CompaniesView(ListCreateAPIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = CompanySerializer

    def get_queryset(self):
        page_nr = int(self.request.query_params.get('page', 0))
        page_size = int(self.request.query_params.get('size', 15))

        page_start = page_nr * page_size
        qs = Company.objects.all()[page_start:page_start + page_size]
        print(qs.query, 'query')
        return qs

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)