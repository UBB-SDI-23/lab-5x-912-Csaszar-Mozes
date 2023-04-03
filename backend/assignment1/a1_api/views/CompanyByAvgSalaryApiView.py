from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView

from ..models import Person, Location, Company, PersonWorkingAtCompany
from ..serializers import (PersonSerializer, LocationSerializer, CompanySerializer, CompanyDetailSerializer,
                          LocationDetailSerializer, PersonWorkingAtCompanySerializer, PersonWorkingAtCompanyDetailSerializer,
                          PersonDetailSerializer, CompanyByAvgSalarySerializer, CompanyNrLocationsSerializer)
from rest_framework.renderers import JSONRenderer
from django.core import serializers
import django.db.models as models


class CompanyByAvgSalaryApiView(APIView):
    #permissions_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        List all the companies that have a rating greater than rating
        '''
        companies = Company.objects.all().annotate(avg_salary=models.Avg('people_working_here__salary', default=0)).order_by('-avg_salary')

        serializer = CompanyByAvgSalarySerializer(companies, many=True)


        return Response(serializer.data, status=status.HTTP_200_OK)
