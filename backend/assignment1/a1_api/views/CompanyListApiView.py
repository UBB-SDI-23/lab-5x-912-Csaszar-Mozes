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


class CompanyListApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]

    def get_object(self, comp_id):
        '''
        Helper method to get the object with given comp_id
        '''
        try:
            return Company.objects.get(id=comp_id)
        except Company.DoesNotExist:
            return None

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the companies for given requested user
        '''
        companies = Company.objects.all().annotate(nr_people_working_here=models.Count("people_working_here", output_field=models.IntegerField()))
        print(companies[0].nr_people_working_here)
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the company with given person data
        '''
        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'start_year': request.data.get('start_year'),
            'net_value': request.data.get('net_value'),
            'reputation': request.data.get('reputation'),
        }
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request, *args, **kwargs):
        comp_id = request.data.get('id')
        if not comp_id:
            return Response(
                {"res": "No ID provided!"},
                status=status.HTTP_400_BAD_REQUEST
            )
        comp_instance = self.get_object(comp_id)
        if not comp_instance:
            return Response(
                {"res": "Object with person id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name', comp_instance.name),
            'description': request.data.get('description', comp_instance.description),
            'start_year': request.data.get('start_year', comp_instance.start_year),
            'net_value': request.data.get('net_value', comp_instance.net_value),
            'reputation': request.data.get('reputation', comp_instance.reputation),
        }
        serializer = CompanySerializer(comp_instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_200_OK)
