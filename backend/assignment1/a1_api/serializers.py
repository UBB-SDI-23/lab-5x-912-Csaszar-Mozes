from datetime import timedelta, datetime

from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework import serializers
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken

from .models import Person, Location, Company, PersonWorkingAtCompany, UserProfile
import django.db.models as models
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class LoginSerializer(TokenObtainPairSerializer):

    def auth(self, attrs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(Q(username__iexact=attrs['username']))
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(attrs['password']):
                return user
        return None

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def validate(self, attrs):
        authenticate_kwargs = {
            'username': attrs[self.username_field],
            'password': attrs['password'],
        }
        try:
            authenticate_kwargs['request'] = self.context['request']
        except KeyError:
            pass
        self.user = self.auth(authenticate_kwargs)
        if self.user is None:
            self.error_messages['no_active_account'] = (
                'No active account found with the given credentials')
            raise AuthenticationFailed(
                self.error_messages['no_active_account'],
                'no_active_account',
            )
        elif not self.user.is_active:
            ac = AccessToken.for_user(self.user)
            expiration_time = datetime.now() + timedelta(minutes=10)
            ac['exp'] = int(expiration_time.timestamp())
            self.error_messages['no_active_account'] = (
                'Account is not active;' + str(ac))
            raise AuthenticationFailed(
                self.error_messages['no_active_account'],
                'no_active_account',
            )
        return super().validate(attrs)

    def create(self, validated_data):
        return super().create(validated_data)


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
        fields = ['id', 'first_name', 'last_name', 'bio', 'university', 'high_school', 'user', 'nr_entities_added']


class CompanySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Company
        fields = ["id", "name", "description", "start_year", "net_value", "reputation", "nr_workers", "nr_locations", "user"]



class LocationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)
    class Meta:
        model = Location
        fields = ["id", "country", "city", "street", "number", "apartment", "company", "description", "user"]


class PersonSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Person
        fields = ["id", "first_name", "last_name", "email", "age", "worker_id", "nr_workplaces", "user"]


class PersonAutocompleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ["id", "first_name", "last_name", "email"]


class PersonWorkingAtCompanySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)

    persons_name = serializers.CharField(read_only=True)
    persons_email = serializers.CharField(read_only=True)
    company_name = serializers.CharField(read_only=True)
    class Meta:
        model = PersonWorkingAtCompany
        fields = ["id", "company", "person", "role", "salary", "persons_name", "persons_email", "company_name", "user"]


class LocationDetailSerializer(serializers.ModelSerializer):
    class CompanySerializer(serializers.ModelSerializer):
        class Meta:
            model = Company
            fields = ["id", "name", "description", "start_year", "net_value", "reputation"]
    company = CompanySerializer(read_only=True)
    user = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Location
        fields = ["id", "country", "city", "street", "number", "apartment", "company", "description", "user"]


class PersonWorkingAtCompanyDetailSerializer(serializers.ModelSerializer):
    class CompanySerializer(serializers.ModelSerializer):

        class Meta:
            model = Company
            fields = ["id", "name", "description", "start_year", "net_value", "reputation"]

    class PersonSerializer(serializers.ModelSerializer):

        class Meta:
            model = Person
            fields = ["id", "first_name", "last_name", "email", "age", "worker_id", "user"]

    person = PersonSerializer(read_only=True)
    company = CompanySerializer(read_only=True)
    user = UserSerializer(read_only=True, many=False)

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
    user = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Company
        fields = ["id", "name", "description", "start_year", "net_value", "reputation", "locations", "people_working_here", "user"]


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
    user = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Person
        fields = ["id", "first_name", "last_name", "email", "age", "worker_id", "working_at_companies", "user"]


class CompanyByAvgSalarySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Company
        fields = ["id", "name", "description", "start_year", "net_value", "reputation", "avg_salary", "user"]


class CompanyNrLocationsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Company
        fields = ["id", "name", "description", "start_year", "net_value", "reputation", "nr_locations", "user"]
