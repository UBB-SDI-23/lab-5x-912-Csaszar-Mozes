from ..api_views.__init__ import *
from ..permissions import IsSafeToView
from ..serializers import IntegerSettingSerializer
from django.contrib.auth.models import User
from ..models import UserProfile, IntegerSetting, UserRoles


class PageSizeView(RetrieveAPIView):
    # add permission to check if user is authenticated
    permission_classes = [IsSafeToView]
    serializer_class = IntegerSettingSerializer

    def get(self, request, *args, **kwargs):
        i_s = IntegerSetting.objects.filter(name='page_size', user_role=UserRoles.ADMIN)
        if i_s.count() == 0:
            return Response({"page_size": 15})
        else:
            return Response({"page_size": i_s[0].value})

