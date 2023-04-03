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


class PersonDetailApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]

    def get_object(self, person_id):
        '''
        Helper method to get the object with given person_id
        '''
        try:
            return Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, person_id, *args, **kwargs):
        '''
        Retrieves the person with given person_id
        '''
        person_instance = self.get_object(person_id)
        if not person_instance:
            return Response(
                {"res": "Object with person id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PersonDetailSerializer(person_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, person_id, *args, **kwargs):
        '''
        Updates the person with given person_id if it exists
        '''
        person_instance = self.get_object(person_id)
        if not person_instance:
            return Response(
                {"res": "Object with person id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'first_name': request.data.get('first_name', person_instance.first_name),
            'last_name': request.data.get('last_name', person_instance.last_name),
            'email': request.data.get('email', person_instance.email),
            'age': request.data.get('age', person_instance.age),
            'worker_id': request.data.get('worker_id', person_instance.income),
        }
        serializer = PersonSerializer(instance=person_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, person_id, *args, **kwargs):
        '''
        Deletes the person with given person_id if exists
        '''
        person_instance = self.get_object(person_id)
        if not person_id:
            return Response(
                {"res": "Object with person id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        person_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

