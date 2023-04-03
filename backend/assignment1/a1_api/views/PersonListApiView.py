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

class PersonListApiView(APIView):
    #permission_classes = [permissions.IsAuthenticated]
    def get_object(self, person_id):
        '''
        Helper method to get the object with given person_id
        '''
        try:
            return Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return None

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the people for given requested user
        '''
        people = Person.objects.annotate(nr_companies=models.Count("working_at_companies", output_field=models.IntegerField()))
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the person with given person data
        '''
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'email': request.data.get('email'),
            'age': request.data.get('age'),
            'worker_id': request.data.get('worker_id'),
        }
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request, *args, **kwargs):
        person_id = request.data.get('id')
        if not person_id:
            return Response(
                {"res": "No ID provided!"},
                status=status.HTTP_400_BAD_REQUEST
            )
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
            'worker_id': request.data.get('worker_id', person_instance.worker_id),
        }
        serializer = PersonSerializer(person_instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_200_OK)

