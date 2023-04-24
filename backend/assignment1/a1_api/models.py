from django.db import models
from django.db.models.functions import Concat
from django.db.models import Value as V
from django.db.models import F, Avg
from django.core import validators

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=2000)
    net_value = models.IntegerField()
    reputation = models.IntegerField(validators=())
    start_year = models.IntegerField(null=True, blank=True, validators=[validators.MinValueValidator(0)])
    avg_salary = models.DecimalField(max_digits=12, decimal_places=4, default=0, null=True)

    @property
    def nr_locations(self):
        return Location.objects.all().filter(company=self.id).aggregate(nr_locations=models.Count('*'))['nr_locations']

    @property
    def nr_workers(self):
        return PersonWorkingAtCompany.objects.all().filter(company=self.id).aggregate(nr_workers=models.Count('*'))['nr_workers']

    def __str__(self):
        return self.name.__str__()

    class Meta:
        indexes = [models.Index(name='ind_company_name_auto', fields=['name', 'id']),
                   models.Index(name='ind_comp_avg_salary', fields=['avg_salary', 'id'])]


class Location(models.Model):
    country = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=100, null=False)
    street = models.CharField(max_length=100, null=False)
    number = models.IntegerField(null=False, validators=[validators.MinValueValidator(0)])
    apartment = models.CharField(max_length=100, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True, related_name="locations")
    description = models.CharField(max_length=5000, null=False, default='')

    def __str__(self):
        return self.country.__str__() + ", " + self.county.null * (self.county.__str__() + ", ") + self.city.__str__() +\
                ", " + self.street.__str__() + ", " + self.number.__str__() + self.apartment.null * (", " + self.apartment.__str__())


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    worker_id = models.IntegerField()
    email = models.EmailField(max_length=75, validators=[validators.EmailValidator()], unique=True)
    age = models.IntegerField()

    @property
    def nr_workplaces(self):
        return PersonWorkingAtCompany.objects.filter(person=self.id).aggregate(nr_workplaces=models.Count('*'))[
            'nr_workplaces']

    def __str__(self):
        return self.first_name.__str__() + " " + self.last_name.__str__()



class PersonWorkingAtCompany(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="working_at_companies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="people_working_here")
    salary = models.IntegerField(validators=[validators.MinValueValidator(0)])
    role = models.CharField(max_length=125)

    class Meta:
        unique_together = [['person', 'company']]
        indexes = [models.Index(name='ind_company', fields=['company'], include=['salary'])]

