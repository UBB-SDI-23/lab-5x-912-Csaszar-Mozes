from rest_framework import serializers
from .models import Person, Location, Company, PersonWorkingAtCompany
import django.db.models as models


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "description", "start_year", "net_value", "reputation", "nr_workers", "nr_locations"]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "country", "county", "city", "street", "number", "apartment", "company"]


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["id", "first_name", "last_name", "email", "age", "worker_id", "nr_workplaces"]


class PersonWorkingAtCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonWorkingAtCompany
        fields = "__all__"


class LocationDetailSerializer(serializers.ModelSerializer):
    class CompanySerializer(serializers.ModelSerializer):
        class Meta:
            model = Company
            fields = ["id", "name", "description", "start_year", "net_value", "reputation"]
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Location
        fields = ["id", "country", "county", "city", "street", "number", "apartment", "company"]


class PersonWorkingAtCompanyDetailSerializer(serializers.ModelSerializer):
    class CompanySerializer(serializers.ModelSerializer):

        class Meta:
            model = Company
            fields = ["id", "name", "description", "start_year", "net_value", "reputation"]

    class PersonSerializer(serializers.ModelSerializer):

        class Meta:
            model = Person
            fields = ["id", "first_name", "last_name", "email", "age", "worker_id"]

    person = PersonSerializer(read_only=True)
    company = CompanySerializer(read_only=True)

    class Meta:
        model = PersonWorkingAtCompany
        fields = '__all__'


class CompanyDetailSerializer(serializers.ModelSerializer):
    class PCforCompanyDetailSerializer(serializers.ModelSerializer):
        class PersonSimpleSerializer(serializers.ModelSerializer):
            class Meta:
                model = Person
                fields = ["id", "first_name", "last_name", "email", "age", "worker_id"]
        person = PersonSimpleSerializer(read_only=True)

        class Meta:
            model = PersonWorkingAtCompany
            fields = ['id', 'person', 'salary', 'role']
    location_ids = LocationSerializer(read_only=True, many=True)
    people_working_here = PCforCompanyDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Company
        fields = ["id", "name", "description", "start_year", "net_value", "reputation", "location_ids", "people_working_here"]


class PersonDetailSerializer(serializers.ModelSerializer):
    class PCforPersonDetailSerializer(serializers.ModelSerializer):
        class CompanySimpleSerializer(serializers.ModelSerializer):
            class Meta:
                model = Company
                fields = ["id", "name", "description", "start_year", "net_value", "reputation"]
        company = CompanySimpleSerializer(read_only=True)

        class Meta:
            model = PersonWorkingAtCompany
            fields = ['id', 'company', 'salary', 'role']
    working_at_companies = PCforPersonDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Person
        fields = ["id", "first_name", "last_name", "email", "age", "worker_id", "working_at_companies"]


class CompanyByAvgSalarySerializer(serializers.ModelSerializer):
    avg_salary = serializers.IntegerField(read_only=True)
    class Meta:
        model = Company
        fields = ["id", "name", "description", "start_year", "net_value", "reputation", "avg_salary"]


class CompanyNrLocationsSerializer(serializers.ModelSerializer):
    nr_locations = serializers.IntegerField(read_only=True)
    class Meta:
        model = Company
        fields = ["id", "name", "description", "start_year", "net_value", "reputation", "nr_locations"]
