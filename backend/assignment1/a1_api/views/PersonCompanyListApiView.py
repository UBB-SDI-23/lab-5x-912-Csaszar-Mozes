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

class PersonCompanyListApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]

    def get_object(self, loc_id):
        '''
        Helper method to get the object with given loc_id
        '''
        try:
            return PersonWorkingAtCompany.objects.get(id=loc_id)
        except PersonWorkingAtCompany.DoesNotExist:
            return None

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the locations for given requested user
        '''
        locations = PersonWorkingAtCompany.objects
        serializer = PersonWorkingAtCompanySerializer(locations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the location with given location data
        '''
        data = {
            'person': request.data.get('person'),
            'company': request.data.get('company'),
            'salary': request.data.get('salary'),
            'role': request.data.get('role'),
        }
        serializer = PersonWorkingAtCompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        pc_id = request.data.get('id')
        if not pc_id:
            return Response(
                {"res": "No ID provided!"},
                status=status.HTTP_400_BAD_REQUEST
            )
        pc_instance = self.get_object(pc_id)
        if not pc_instance:
            return Response(
                {"res": "Object with pc id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'person': request.data.get('person', pc_instance.person),
            'company': request.data.get('company', pc_instance.company),
            'salary': request.data.get('salary', pc_instance.salary),
            'role': request.data.get('role', pc_instance.role),
        }
        serializer = PersonWorkingAtCompanySerializer(pc_instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_200_OK)

