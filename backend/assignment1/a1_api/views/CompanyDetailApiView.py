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

class CompanyDetailApiView(APIView):
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

    # 3. Retrieve
    def get(self, request, comp_id, *args, **kwargs):
        '''
        Retrieves the person with given person_id
        '''
        comp_instance = self.get_object(comp_id)
        if not comp_instance:
            return Response(
                {"res": "Object with location id does not exist!"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CompanyDetailSerializer(comp_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, comp_id, *args, **kwargs):
        '''
        Updates the company with given comp_id if it exists
        '''
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

    # 5. Delete
    def delete(self, request, comp_id, *args, **kwargs):
        '''
        Deletes the company with given comp_id if exists
        '''
        comp_instance = self.get_object(comp_id)
        if not comp_id:
            return Response(
                {"res": "Object with company id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        comp_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

