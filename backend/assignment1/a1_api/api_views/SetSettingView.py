from rest_framework.permissions import IsAuthenticated

from ..api_views.__init__ import *
from ..permissions import IsAdministrator
from ..serializers import IntegerSettingSerializer
from django.contrib.auth.models import User
from ..models import UserProfile, IntegerSetting, UserRoles


class SetSettingView(CreateAPIView):
    # add permission to check if user is authenticated
    permission_classes = [IsAdministrator]
    serializer_class = IntegerSettingSerializer

    def post(self, request, *args, **kwargs):
        user_id = request.user.id
        value = request.data['value']
        name = request.data['name']
        user_role = request.data['user_role']
        i_s = IntegerSetting.objects.filter(name=name, user_id=user_id)
        if i_s.count() == 0:
            new_i_s = IntegerSetting.objects.create(user_id=user_id, value=value,name=name,user_role=user_role)
            new_i_s.save()
        else:
            old_i_s = i_s[0]
            old_i_s = IntegerSettingSerializer(instance=old_i_s, data={'value': value})
            old_i_s.value = value
            if old_i_s.is_valid():
                old_i_s.save()
        return Response({"message": "Setting changed successfully!"})

