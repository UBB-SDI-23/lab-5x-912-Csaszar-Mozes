from ..api_views.__init__ import *
from ..serializers import PersonSerializer
from ..models import Person
import django.db.models as models
from django.db.models import Value as V
from django.db.models.functions import Concat


class PersonNameAutoView(ListAPIView):
    #permissions_classes = [permissions.IsAuthenticated]
    serializer_class = PersonSerializer
    def get_queryset(self):
        page_size = int(self.request.query_params.get('size', 15))
        name = self.request.query_params.get('name', '')
        return Person.objects.annotate(name=Concat('first_name', V(' '), 'last_name')).filter(name__icontains=name)[:page_size]
