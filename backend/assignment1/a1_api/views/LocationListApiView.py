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
class LocationListApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]

    def get_object(self, loc_id):
        '''
        Helper method to get the object with given loc_id
        '''
        try:
            return Location.objects.get(id=loc_id)
        except Location.DoesNotExist:
            return None

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the locations for given requested user
        '''
        locations = Location.objects
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the location with given location data
        '''
        data = {
            'country': request.data.get('country'),
            'county': request.data.get('county', ""),
            'city': request.data.get('city'),
            'street': request.data.get('street'),
            'number': request.data.get('number'),
            'apartment': request.data.get('apartment', ""),
            'company': request.data.get('company', None),

        }
        serializer = LocationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        loc_id = request.data.get('id')
        if not loc_id:
            return Response(
                {"res": "No ID provided!"},
                status=status.HTTP_400_BAD_REQUEST
            )
        loc_instance = self.get_object(loc_id)
        if not loc_instance:
            return Response(
                {"res": "Object with location id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'country': request.data.get('country', loc_instance.country),
            'county': request.data.get('county', loc_instance.county),
            'city': request.data.get('city', loc_instance.city),
            'street': request.data.get('street', loc_instance.street),
            'number': request.data.get('number', loc_instance.number),
            'apartment': request.data.get('apartment', loc_instance.apartment),
            'company': request.data.get('company', loc_instance.company),
        }
        serializer = LocationSerializer(loc_instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_200_OK)

