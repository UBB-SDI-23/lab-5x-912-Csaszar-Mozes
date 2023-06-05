from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView,\
    RetrieveAPIView, get_object_or_404, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from ..permissions import IsSafeToView
from ..serializers import CompanySerializer
from ..models import Company
import tensorflow as tf


class CompaniesView(ListCreateAPIView):
    pass

