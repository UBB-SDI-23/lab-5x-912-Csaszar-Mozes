from ..api_views.__init__ import *
from ..permissions import IsSafeToView
from ..serializers import PersonAutocompleteSerializer
from ..models import Person
import django.db.models as models
from django.db.models import Value as V
from django.db.models.functions import Concat


class PersonNameAutoView(ListAPIView):
    permissions_classes = [IsSafeToView]
    serializer_class = PersonAutocompleteSerializer
    def get_queryset(self):
        page_size = int(self.request.query_params.get('size', 15))
        name = self.request.query_params.get('name', '')
        return Person.objects.annotate(name=Concat('first_name', V(' '), 'last_name')).filter(name__icontains=name).values("id", "first_name", "last_name", "email")[:page_size]
