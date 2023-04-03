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

class PersonCompanyDetailApiView(APIView):
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

    # 3. Retrieve
    def get(self, request, pc_id, *args, **kwargs):
        '''
        Retrieves the person with given person_id
        '''
        pc_instance = self.get_object(pc_id)
        if not pc_instance:
            return Response(
                {"res": "Object with location id does not exist!"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PersonWorkingAtCompanyDetailSerializer(pc_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, pc_id, *args, **kwargs):
        '''
            Updates the pc element with given pc_id if it exists
        '''
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
        serializer = LocationSerializer(pc_instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 5. Delete
    def delete(self, request, pc_id, *args, **kwargs):
        '''
        Deletes the location with given loc_id if exists
        '''
        pc_instance = self.get_object(loc_id=pc_id)
        if not pc_instance:
            return Response(
                {"res": "Object with pc id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        pc_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
