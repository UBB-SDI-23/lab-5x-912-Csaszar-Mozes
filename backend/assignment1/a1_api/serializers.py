from rest_framework import serializers
from .models import Person, Location, Company, PersonWorkingAtCompany, UserProfile
import django.db.models as models
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class ConfirmRegisterSerializer(serializers.Serializer):
    message = serializers.CharField(read_only=True)



class RegisterMessageSerializer(serializers.Serializer):
    activation_token = serializers.CharField(read_only=True)


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match!"})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.is_active = False
        user.save()

        user_profile = UserProfile.objects.create(
            user=user
        )
        user_profile.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active']


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "description", "start_year", "net_value", "reputation", "nr_workers", "nr_locations"]



class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "country", "city", "street", "number", "apartment", "company", "description"]


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["id", "first_name", "last_name", "email", "age", "worker_id", "nr_workplaces"]


class PersonAutocompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["id", "first_name", "last_name", "email"]


class PersonWorkingAtCompanySerializer(serializers.ModelSerializer):
    persons_name = serializers.CharField(read_only=True)
    persons_email = serializers.CharField(read_only=True)
    company_name = serializers.CharField(read_only=True)
    class Meta:
        model = PersonWorkingAtCompany
        fields = ["id", "company", "person", "role", "salary", "persons_name", "persons_email", "company_name"]


class LocationDetailSerializer(serializers.ModelSerializer):
    class CompanySerializer(serializers.ModelSerializer):
        class Meta:
            model = Company
            fields = ["id", "name", "description", "start_year", "net_value", "reputation"]
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Location
        fields = ["id", "country", "city", "street", "number", "apartment", "company", "description"]


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
    locations = LocationSerializer(read_only=True, many=True)
    people_working_here = PCforCompanyDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Company
        fields = ["id", "name", "description", "start_year", "net_value", "reputation", "locations", "people_working_here"]


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
    class Meta:
        model = Company
        fields = ["id", "name", "description", "start_year", "net_value", "reputation", "avg_salary"]


class CompanyNrLocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "description", "start_year", "net_value", "reputation", "nr_locations"]
