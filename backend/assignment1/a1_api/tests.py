from django.test import TestCase
from rest_framework.test import  APITestCase
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from django.urls import reverse
from .models import Person, Company, Location, PersonWorkingAtCompany


# Create your tests here.
class TestPeopleView(APITestCase):
    url = '/api/people/'

    def setUp(self) -> None:
        Person.objects.create(
            first_name="Test", last_name="Test", worker_id=11, age=44, email="test@test.test"
        )
    def test_get(self):
        result = self.client.get(self.url)
        self.assertEqual(result.status_code, HTTP_200_OK)

    def test_post(self):
        result = self.client.post(self.url, {"first_name": "Ifrim","last_name": "Miculescu","email": "ifrimm23@yahoo.ro","age": 25,"worker_id": 14720})
        self.assertEqual(result.status_code, HTTP_201_CREATED)

    def test_put(self):
        result = self.client.put(self.url, {"id": 1,"first_name": "Ifrim","last_name": "Miculescu","email": "ifrimm23@yahoo.ro","age": 25,"worker_id": 14720})
        self.assertEqual(result.status_code, HTTP_200_OK)
        result = self.client.put(self.url, {"first_name": "Ifrim", "last_name": "Miculescu",
                                            "email": "ifrimm23@yahoo.ro", "age": 25, "worker_id": 14720})
        self.assertEqual(result.status_code, HTTP_400_BAD_REQUEST)


class TestPeopleIDView(APITestCase):
    url = '/api/people/1/'

    def setUp(self) -> None:
        Person.objects.create(
            first_name="Test", last_name="Test", worker_id=11, age=44, email="test@test.test"
        )
    def test_get(self):
        result = self.client.get(self.url)
        self.assertEqual(result.status_code, HTTP_200_OK)
        result = self.client.get('/api/people/2/')
        self.assertEqual(result.status_code, HTTP_400_BAD_REQUEST)

    def test_put(self):
        result = self.client.put(self.url, {"first_name": "Ifrim","last_name": "Miculescu",
                                            "email": "ifrimm23@yahoo.ro","age": 25,"worker_id": 14720})
        self.assertEqual(result.status_code, HTTP_200_OK)
        result = self.client.put('/api/people/2/', {"first_name": "Ifrim", "last_name": "Miculescu",
                                            "email": "ifrimm23@yahoo.ro", "age": 25, "worker_id": 14720})
        self.assertEqual(result.status_code, HTTP_400_BAD_REQUEST)

    def test_delete(self):
        result = self.client.delete(self.url)
        self.assertEqual(result.status_code, HTTP_200_OK)
        result = self.client.delete(self.url)
        self.assertEqual(result.status_code, HTTP_400_BAD_REQUEST)


class TestCompaniesView(APITestCase):
    url = '/api/companies/'

    def setUp(self) -> None:
        Company.objects.create(
            name="test", description="test", start_year=1, net_value=1, reputation=1
        )
    def test_get(self):
        result = self.client.get(self.url)
        self.assertEqual(result.status_code, HTTP_200_OK)

    def test_post(self):
        result = self.client.post(self.url, {"name": "Memo 10",
                                            "description": "A self-serv restaurant catered towards students and physical laborers",
                                            "start_year": 2000,"net_value": 100000,"reputation": 90,"nr_people_working_here": 1})
        self.assertEqual(result.status_code, HTTP_201_CREATED)

    def test_put(self):
        result = self.client.put(self.url, {"id": 1, "name": "Memo 10",
                                            "description": "A self-serv restaurant catered towards students and physical laborers",
                                            "start_year": 2000,"net_value": 100000,"reputation": 90,"nr_people_working_here": 1})
        self.assertEqual(result.status_code, HTTP_200_OK)
        result = self.client.put(self.url, {"name": "Memo 10",
                                            "description": "A self-serv restaurant catered towards students and physical laborers",
                                            "start_year": 2000,"net_value": 100000,"reputation": 90,"nr_people_working_here": 1})
        self.assertEqual(result.status_code, HTTP_400_BAD_REQUEST)


class TestCompaniesIDView(APITestCase):
    url = '/api/companies/1/'

    def setUp(self) -> None:
        Company.objects.create(
            name="test", description="test", start_year=1, net_value=1, reputation=1
        )
    def test_get(self):
        result = self.client.get(self.url)
        self.assertEqual(result.status_code, HTTP_200_OK)
        result = self.client.get('/api/companies/2/')
        self.assertEqual(result.status_code, HTTP_400_BAD_REQUEST)

    def test_put(self):
        result = self.client.put(self.url, {"name": "Memo 10",
                                            "description": "A self-serv restaurant catered towards students and physical laborers",
                                            "start_year": 2000,"net_value": 100000,"reputation": 90,"nr_people_working_here": 1})
        self.assertEqual(result.status_code, HTTP_200_OK)
        result = self.client.put('/api/companies/2/', {"name": "Memo 10",
                                            "description": "A self-serv restaurant catered towards students and physical laborers",
                                            "start_year": 2000,"net_value": 100000,"reputation": 90,"nr_people_working_here": 1})
        self.assertEqual(result.status_code, HTTP_400_BAD_REQUEST)

    def test_delete(self):
        result = self.client.delete(self.url)
        self.assertEqual(result.status_code, HTTP_200_OK)
        result = self.client.delete(self.url)
        self.assertEqual(result.status_code, HTTP_400_BAD_REQUEST)


class TestLocationsView(APITestCase):
    url = '/api/locations/'

    def setUp(self) -> None:
        Company.objects.create(
            name="test", description="test", start_year=1, net_value=1, reputation=1
        )
        Location.objects.create(
            country="Test", county="Test", city="test", street="test", number=1, apartment="test",
            company=Company.objects.all()[0]
        )
    def test_get(self):
        result = self.client.get(self.url)
        self.assertEqual(result.status_code, HTTP_200_OK)

    def test_post(self):
        result = self.client.post(self.url, {"country": "Romania","county": "Cluj",
                                             "city": "Cluj Napoca","street": "Frunzisului","number": 106,"apartment": "","company": 1})
        self.assertEqual(result.status_code, HTTP_201_CREATED)

    def test_put(self):
        result = self.client.put(self.url, {"id": 1, "country": "Romania","county": "Cluj",
                                            "city": "Cluj Napoca","street": "Frunzisului","number": 106,"apartment": "","company": 1})
        self.assertEqual(result.status_code, HTTP_200_OK)
        result = self.client.put(self.url, {"country": "Romania","county": "Cluj",
                                            "city": "Cluj Napoca","street": "Frunzisului","number": 106,"apartment": "","company": 1})
        self.assertEqual(result.status_code, HTTP_400_BAD_REQUEST)


class TestLocationsIDView(APITestCase):
    url = '/api/locations/1/'

    def setUp(self) -> None:
        Company.objects.create(
            name="test", description="test", start_year=1, net_value=1, reputation=1
        )
        Location.objects.create(
            country="Test", county="Test", city="test", street="test", number=1, apartment="test",
            company=Company.objects.all()[0]
        )
    def test_get(self):
        result = self.client.get(self.url)
        self.assertEqual(result.status_code, HTTP_200_OK)
        result = self.client.get('/api/locations/2/')
        self.assertEqual(result.status_code, HTTP_400_BAD_REQUEST)

    def test_put(self):
        result = self.client.put(self.url, {"country": "Romania","county": "Cluj",
                                            "city": "Cluj Napoca","street": "Frunzisului","number": 106,"apartment": "","company": 1})
        self.assertEqual(result.status_code, HTTP_200_OK)
        result = self.client.put('/api/locations/2/', {"country": "Romania","county": "Cluj",
                                                    "city": "Cluj Napoca","street": "Frunzisului","number": 106,"apartment": "","company": 1})
        self.assertEqual(result.status_code, HTTP_400_BAD_REQUEST)

    def test_delete(self):
        result = self.client.delete(self.url)
        self.assertEqual(result.status_code, HTTP_200_OK)
        result = self.client.delete(self.url)
        self.assertEqual(result.status_code, HTTP_400_BAD_REQUEST)


class TestPeopleCompaniesView(APITestCase):
    url = '/api/pc/'

    def setUp(self) -> None:
        Company.objects.create(
            name="test", description="test", start_year=1, net_value=1, reputation=1
        )
        Person.objects.create(
            first_name="Test", last_name="Test", worker_id=11, age=44, email="test@test.test"
        )
        Person.objects.create(
            first_name="Test", last_name="Test", worker_id=11, age=44, email="test@test.test"
        )

        PersonWorkingAtCompany.objects.create(
            person=Person.objects.all()[0], company=Company.objects.all()[0], salary=1, role="test"
        )
    def test_get(self):
        result = self.client.get(self.url)
        self.assertEqual(result.status_code, HTTP_200_OK)

    def test_post(self):
        result = self.client.post(self.url, {"person": 2,"company": 1,"salary": 19000,"role": "CEO"})
        self.assertEqual(result.status_code, HTTP_201_CREATED)

    def test_put(self):
        result = self.client.put(self.url, {"id": 1, "person": 1,"company": 1,"salary": 19000,"role": "CEO"})
        self.assertEqual(result.status_code, HTTP_200_OK)
        result = self.client.put(self.url, {"person": 1,"company": 1,"salary": 19000,"role": "CEO"})
        self.assertEqual(result.status_code, HTTP_400_BAD_REQUEST)


class TestPeopleCompaniesIDView(APITestCase):
    url = '/api/pc/1/'

    def setUp(self) -> None:
        Company.objects.create(
            name="test", description="test", start_year=1, net_value=1, reputation=1
        )
        Person.objects.create(
            first_name="Test", last_name="Test", worker_id=11, age=44, email="test@test.test"
        )

        PersonWorkingAtCompany.objects.create(
            person=Person.objects.all()[0], company=Company.objects.all()[0], salary=1, role="test"
        )
    def test_get(self):
        result = self.client.get(self.url)
        self.assertEqual(result.status_code, HTTP_200_OK)
        result = self.client.get('/api/pc/2/')
        self.assertEqual(result.status_code, HTTP_400_BAD_REQUEST)

    def test_put(self):
        result = self.client.put(self.url, {"person": 1,"company": 1,"salary": 19000,"role": "CEO"})
        self.assertEqual(result.status_code, HTTP_200_OK)
        result = self.client.put('/api/pc/2/', {"person": 1,"company": 1,"salary": 19000,"role": "CEO"})
        self.assertEqual(result.status_code, HTTP_400_BAD_REQUEST)

    def test_delete(self):
        result = self.client.delete(self.url)
        self.assertEqual(result.status_code, HTTP_200_OK)
        result = self.client.delete(self.url)
        self.assertEqual(result.status_code, HTTP_400_BAD_REQUEST)


class TestAvgSalaryFunctionality(APITestCase):

    def test_avg_salary(self):
        result = self.client.get('/api/companies/avg-salary/')
        # Test if request got through
        self.assertEqual(result.status_code, HTTP_200_OK)
        # Test number of returned elements
        self.assertEqual(len(result.data), 0)
        def setUp():
            Person.objects.create(
                first_name="Test", last_name="Test", worker_id=11, age=44, email="test@test.test"
            )
            Person.objects.create(
                first_name="Test", last_name="Test", worker_id=11, age=44, email="test@test.test"
            )
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
                person=Person.objects.all()[1], company=Company.objects.all()[0], salary=100, role="test"
            )
            PersonWorkingAtCompany.objects.create(
                person=Person.objects.all()[2], company=Company.objects.all()[0], salary=1000, role="test"
            )
            PersonWorkingAtCompany.objects.create(
                person=Person.objects.all()[0], company=Company.objects.all()[2], salary=5000, role="test"
            )
            PersonWorkingAtCompany.objects.create(
                person=Person.objects.all()[1], company=Company.objects.all()[2], salary=1, role="test"
            )
        setUp()
        result = self.client.get('/api/companies/avg-salary/')
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
        result = self.client.get('/api/companies/nr-locations/')
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