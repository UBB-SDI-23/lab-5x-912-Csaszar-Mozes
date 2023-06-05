from rest_framework.generics import RetrieveAPIView, get_object_or_404, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from ...permissions import IsSafeToView
from ...serializers import MessageSerializer
import tensorflow as tf


class CompaniesView(RetrieveAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsSafeToView | permissions.IsAuthenticated]

