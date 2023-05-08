import os

from rest_framework.exceptions import ValidationError

from ..api_views.__init__ import *
from ..permissions import IsAdministrator
from ..serializers import PersonSerializer
from ..models import Person, Company, PersonWorkingAtCompany, Location
from django.db.models import Max
import psycopg2
import faker as fk
import random as rnd

fake = fk.Faker()


def escape_single_quote(string):
    new_str = ''
    for let in string:
        if let == "'":
            new_str += "''"
        elif let == ",":
            new_str += ""
        else:
            new_str += let
    return new_str


def generate_p(worker_id, user_id):
    first_name = escape_single_quote(fake.first_name())
    last_name = escape_single_quote(fake.last_name())
    email = f"{first_name.lower()}.{last_name.lower()}@{fake.domain_name()}"
    age = rnd.randint(18, 100)
    while Person.objects.filter(email=email).count() != 0:
        email = f"{first_name.lower()}.{last_name.lower()}{rnd.randint(1,10000)}@{fake.domain_name()}"
    worker_id += 3
    new_p = Person.objects.create(first_name=first_name, last_name=last_name, email=email, age=age, worker_id=worker_id, user_id=user_id)
    new_p.save()
    return worker_id

def generate_c(user_id):
    name = escape_single_quote(fake.company())
    description = escape_single_quote(fake.catch_phrase())
    start_year = rnd.randint(1750, 2023)
    net_value = rnd.randint(100, 100000)
    reputation = rnd.randint(20,100)
    while Company.objects.filter(name=name):
        name += str(rnd.randint(0, 9))
    new_c = Company.objects.create(name=name, description=description, start_year=start_year, net_value=net_value, reputation=reputation, user_id=user_id)
    new_c.save()
    return

def generate_pc(c_id_range, p_id_range, nr, user_id):
    used = {}
    for _ in range(nr):
        role = escape_single_quote(fake.job())
        salary = rnd.randint(100, 100000)
        c_id = rnd.randint(c_id_range[0], c_id_range[1])
        p_id = rnd.randint(p_id_range[0], p_id_range[1])
        while used.get(str((p_id, c_id)), None) is not None:
            c_id = rnd.randint(c_id_range[0], c_id_range[1])
            p_id = rnd.randint(p_id_range[0], p_id_range[1])
        used[str((p_id, c_id))] = True
        new_pc = PersonWorkingAtCompany.objects.create(role=role,user_id=user_id, salary=salary, person_id=p_id, company_id=c_id)
        new_pc.save()

def generate_l(nr, c_id_range):
    for _ in range(nr):
        c_id = rnd.randint(c_id_range[0], c_id_range[1])
        country = escape_single_quote(fake.country())
        city = escape_single_quote(fake.city())
        street = escape_single_quote(fake.street_name())
        apartment = str(rnd.randint(1, 10000)) if rnd.random() < 0.5 else ""
        number = str(rnd.randint(1, 10000))
        description = escape_single_quote(fake.paragraph(nb_sentences=10, variable_nb_sentences=True))
        new_l = Location.objects.create(country=country,city=city,street=street,apartment=apartment,number=number,description=description,company_id=c_id)
        new_l.save()
    return

class GenerateDataView(CreateAPIView):
    permission_classes = [IsAdministrator]
    serializer_class = PersonSerializer

    def post(self, request, *args, **kwargs):
        chances = [0.9, 0.097, 0.0027, 0.000297, 0.000003]
        chances_added = [0]
        for i in range(len(chances)):
            chances_added.append(chances_added[i] + chances[i])
        chances_added.append(1)
        nr_people_in_comp = [1, 5, 10, 20, 45, 100]
        nr_locations_in_comp = [1, 2, 4, 7, 12, 30]
        net_values = [100, 1000, 15764, 547895, 7845962, 54687514]
        salaries = [100, 250, 2500, 25000, 180000, 600000]
        reputations = [20, 60, 70, 80, 90, 100]

        nr_c = request.data.get('nr_c', 0)
        nr_p = request.data.get('nr_p', 0)
        nr_l = request.data.get('nr_l', 0)
        nr_pc = request.data.get('nr_pc', 0)
        if nr_c < 10 or nr_p < 10:
            return Response({"message": "Number of companies and people generated should be greater than 10!"}, status=400)
        if nr_c > 100 or nr_p > 100:
            return Response({"message": "Number of companies and people generated should be less than 100!"}, status=400)
        if nr_pc > nr_c * nr_p // 4:
            return Response({"message": "Person times company should be four times bigger than the number of people working at a company!"}, status=400)

        c_ind = Company.objects.aggregate(max_id=Max('id'))['max_id'] + 1
        p_ind = Person.objects.aggregate(max_id=Max('id'))['max_id'] + 1
        worker_id = Person.objects.aggregate(max_id=Max('worker_id'))['max_id']

        c_id_range = [c_ind, c_ind + nr_c]
        p_id_range = [p_ind, p_ind + nr_p]
        for _ in range(nr_p):
            worker_id = generate_p(worker_id, self.request.user.id)
        for _ in range(nr_c):
            generate_c(self.request.user.id)
        generate_pc(c_id_range, p_id_range, nr_pc, self.request.user.id)
        generate_l(nr_l, c_id_range)

        return Response({"message": "Data successfully generated."}, status=200)
