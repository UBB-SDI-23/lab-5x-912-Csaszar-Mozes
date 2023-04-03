from django.test import TestCase
from rest_framework.test import  APITestCase
from rest_framework.status import HTTP_200_OK
from django.urls import reverse
from .models import Person, Company, Location, PersonWorkingAtCompany

# Create your tests here.

class EndPointsWorkingTestCase(APITestCase):

    def setUp(self) -> None:
        Person.objects.create(
            first_name="Test", last_name="Test", worker_id=11, age=44, email="test@test.test"
        )
        Company.objects.create(
            name="test", description="test", start_year=1, net_value=1, reputation=1
        )
        Location.objects.create(
            country="Test", county="Test", city="test", street="test", number=1, apartment="test", company=Company.objects.all()[0]
        )
        PersonWorkingAtCompany.objects.create(
            person=Person.objects.all()[0], company=Company.objects.all()[0], salary=1, role="test"
        )
    def test_urls(self):
        url_list = [
            '/people/', '/people/1/', '/locations/', '/locations/1/', '/companies/', '/companies/1/',
            '/companies/reputation-greater-than/10/', '/pc/', '/pc/1/', '/companies/avg-salary/',
            '/companies/nr-locations/'
        ]

        for name in url_list:
            result = self.client.get(name)
            self.assertEqual(result.status_code, HTTP_200_OK)
            print(name, "is open.")


class TestAvgSalaryFunctionality(APITestCase):
    def setUp(self) -> None:
        Person.objects.create(
            first_name="Test", last_name="Test", worker_id=11, age=44, email="test@test.test"
        )
        Company.objects.create(
            name="c1", description="test", start_year=1, net_value=1, reputation=1
        )
        Company.objects.create(
            name="c2", description="test", start_year=1, net_value=1, reputation=1
        )
        Company.objects.create(
            name="c3", description="test", start_year=1, net_value=1, reputation=1
        )
        Location.objects.create(
            country="Test", county="Test", city="test", street="test", number=1, apartment="test",
            company=Company.objects.all()[0]
        )
        PersonWorkingAtCompany.objects.create(
            person=Person.objects.all()[0], company=Company.objects.all()[0], salary=100, role="test"
        )
        PersonWorkingAtCompany.objects.create(
            person=Person.objects.all()[0], company=Company.objects.all()[0], salary=1000, role="test"
        )
        PersonWorkingAtCompany.objects.create(
            person=Person.objects.all()[0], company=Company.objects.all()[2], salary=5000, role="test"
        )
        PersonWorkingAtCompany.objects.create(
            person=Person.objects.all()[0], company=Company.objects.all()[2], salary=1, role="test"
        )

    def test_avg_salary(self):
        result = self.client.get('/companies/avg-salary/')
        #Test if request got through
        self.assertEqual(result.status_code, HTTP_200_OK)
        #Test number of returned elements
        self.assertEqual(len(result.data), 3)
        #Test order
        self.assertEqual(result.data[0]['id'], Company.objects.all()[2].id)
        self.assertEqual(result.data[1]['id'], Company.objects.all()[0].id)
        self.assertEqual(result.data[2]['id'], Company.objects.all()[1].id)
        #Test for correct avg_salary
        self.assertEqual(result.data[0]['avg_salary'], 2500)
        self.assertEqual(result.data[1]['avg_salary'], 550)
        self.assertEqual(result.data[2]['avg_salary'], 0)


class TestNrLocationsFunctionality(APITestCase):
    def setUp(self) -> None:
        Company.objects.create(
            name="c1", description="test", start_year=1, net_value=1, reputation=1
        )
        Company.objects.create(
            name="c2", description="test", start_year=1, net_value=1, reputation=1
        )
        Company.objects.create(
            name="c3", description="test", start_year=1, net_value=1, reputation=1
        )
        Location.objects.create(
            country="Test", county="Test", city="test", street="test", number=1, apartment="test",
            company=Company.objects.all()[1]
        )
        Location.objects.create(
            country="Test", county="Test", city="test", street="test", number=1, apartment="test",
            company=Company.objects.all()[2]
        )
        Location.objects.create(
            country="Test", county="Test", city="test", street="test", number=1, apartment="test",
            company=Company.objects.all()[2]
        )
        Location.objects.create(
            country="Test", county="Test", city="test", street="test", number=1, apartment="test",
            company=Company.objects.all()[2]
        )

    def test_avg_salary(self):
        result = self.client.get('/companies/nr-locations/')
        #Test if request got through
        self.assertEqual(result.status_code, HTTP_200_OK)
        #Test number of returned elements
        self.assertEqual(len(result.data), 3)
        #Test order
        self.assertEqual(result.data[0]['id'], Company.objects.all()[2].id)
        self.assertEqual(result.data[1]['id'], Company.objects.all()[1].id)
        self.assertEqual(result.data[2]['id'], Company.objects.all()[0].id)
        #Test for correct nr_locations
        self.assertEqual(result.data[0]['nr_locations'], 3)
        self.assertEqual(result.data[1]['nr_locations'], 1)
        self.assertEqual(result.data[2]['nr_locations'], 0)