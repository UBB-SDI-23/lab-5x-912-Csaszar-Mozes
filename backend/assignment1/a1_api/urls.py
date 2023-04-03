
from django.urls import path, include
from .views import (
    PeopleView, PeopleIDView, LocationsView, LocationsIDView, CompaniesView,
    CompaniesIDView, CompanyReputationGTView, PersonCompanyView, PersonCompanyIDView,
    CompanyByAvgSalaryApiView, CompanyByNrLocationsApiView, PeopleIDCompaniesView, PeopleIDCompaniesIDView,
    CompaniesIDPeopleView, CompaniesIDPeopleIDView
)



urlpatterns = [
    path('people/', PeopleView.as_view(), name="people_list"),
    path('people/<int:person_id>/', PeopleIDView.as_view(), name="people_detail"),
    path('people/<int:person_id>/companies/', PeopleIDCompaniesView.as_view(), name="peopleidcompanies"),
    path('people/<int:person_id>/companies/<int:comp_id>/', PeopleIDCompaniesIDView.as_view(), name="peopleidcompaniesid"),
    path('locations/', LocationsView.as_view(), name="locations_list"),
    path('locations/<int:loc_id>/', LocationsIDView.as_view(), name="locations_detail"),
    path('companies/', CompaniesView.as_view(), name="companies_list"),
    path('companies/<int:comp_id>/', CompaniesIDView.as_view(), name="companies_detail"),
    path('companies/<int:comp_id>/people/', CompaniesIDPeopleView.as_view(), name="companiesidpeople"),
    path('companies/<int:comp_id>/people/<int:person_id>/', CompaniesIDPeopleIDView.as_view(), name="companiesidpeopleid"),
    path('companies/reputation-greater-than/<int:reputation>/', CompanyReputationGTView.as_view(), name="companies_reputation_gt"),
    path('pc/', PersonCompanyView.as_view(), name="pc_list"),
    path('pc/<int:pc_id>/', PersonCompanyIDView.as_view(), name="pc_detail"),
    path('companies/avg-salary/', CompanyByAvgSalaryApiView.as_view(), name="companies_avg_salary"),
    path('companies/nr-locations/', CompanyByNrLocationsApiView.as_view(), name="companies_nr_locations")
]