from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Person, Location, Company, PersonWorkingAtCompany
from .serializers import (PersonSerializer, LocationSerializer, CompanySerializer, CompanyDetailSerializer,
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


class LocationDetailApiView(APIView):
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

    # 3. Retrieve
    def get(self, request, loc_id, *args, **kwargs):
        '''
        Retrieves the person with given person_id
        '''
        loc_instance = self.get_object(loc_id)
        if not loc_instance:
            return Response(
                {"res": "Object with location id does not exist!"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = LocationDetailSerializer(loc_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, loc_id, *args, **kwargs):
        '''
            Updates the person with given loc_id if it exists
        '''
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

    # 5. Delete
    def delete(self, request, loc_id, *args, **kwargs):
        '''
        Deletes the location with given loc_id if exists
        '''
        loc_instance = self.get_object(loc_id=loc_id)
        if not loc_instance:
            return Response(
                {"res": "Object with location id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        loc_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


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


class CompanyFilterApiView(APIView):
    #permissions_classes = [permissions.IsAuthenticated]

    def get(self, request, reputation, *args, **kwargs):
        '''
        List all the companies that have a rating greater than rating
        '''
        company = Company.objects.filter(reputation__gt=reputation)
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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


class CompanyByAvgSalaryApiView(APIView):
    #permissions_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        List all the companies that have a rating greater than rating
        '''
        companies = Company.objects.all().annotate(avg_salary=models.Avg('people_working_here__salary', default=0)).order_by('-avg_salary')

        serializer = CompanyByAvgSalarySerializer(companies, many=True)


        return Response(serializer.data, status=status.HTTP_200_OK)


class CompanyNrLocationsApiView(APIView):
    permissions_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        List all the companies that have a rating greater than rating
        '''
        company = Company.objects.all().\
            annotate(nr_locations=models.Count('location_id')). \
            order_by('-nr_locations')
        serializer = CompanyNrLocationsSerializer(company, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)