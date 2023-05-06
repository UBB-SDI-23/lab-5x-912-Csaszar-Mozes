from ..api_views.__init__ import *
from ..serializers import UserProfileSerializer
from ..models import UserProfile


class PersonalProfileView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.all()

    def get_object(self):
        try:
            print(self.get_queryset().get(user__id=self.request.user.id))
            return self.get_queryset().get(user__id=self.request.user.id)
        except UserProfile.DoesNotExist:
            return {"ERROR": "No such user profile found!"}

    def put(self, request, *args, **kwargs):
        user = list(UserProfile.objects.all().filter(user__id=self.request.user.id))[0]
        user.last_name = request.data['last_name']
        user.first_name = request.data['first_name']
        user.bio = request.data['bio']
        user.university = request.data['university']
        user.high_school = request.data['high_school']
        user.save()
        print(request.data)
        print(user)
        return Response({"message": "User profile updated successfully!"}, status=200)

    def delete(self, request, *args, **kwargs):
        # Reset user profile
        user = UserProfile.objects.get(user__id=self.request.user.id)
        user.last_name = ''
        user.first_name = ''
        user.bio = ''
        user.university = ''
        user.high_school = ''
        user.save()
        return Response({"message": "Profile reset successfully"}, status=200)
