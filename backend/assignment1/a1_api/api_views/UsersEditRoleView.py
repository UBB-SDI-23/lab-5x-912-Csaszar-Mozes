from rest_framework.exceptions import ValidationError

from ..api_views.__init__ import *
from ..permissions import IsAdministrator
from ..serializers import MessageSerializer
from django.contrib.auth.models import User
from ..models import UserProfile


class UsersEditRoleView(UpdateAPIView):
    # add permission to check if user is authenticated
    permission_classes = [IsAdministrator]
    serializer_class = MessageSerializer

    def get_queryset(self):
        return UserProfile.objects.all()

    def put(self, request, *args, **kwargs):
        print(request.data)
        user_id = int(request.data['user_id'])
        role = int(request.data['role'])
        if 0 < role < 4:
            try:
                user_p = UserProfile.objects.get(user_id=user_id)
                user_p.role = role
                user_p.save()
            except UserProfile.DoesNotExist:
                raise ValidationError("No user with given id!")
        else:
            raise ValidationError("Role should be an integer between 1 and 3 (both ends inclusive)!")
        return Response({"message": "User role updated successfully!"}, status=200)

    def patch(self, request, *args, **kwargs):
        pass
